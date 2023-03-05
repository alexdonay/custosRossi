from flask import *
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
index = Blueprint('index', __name__)
@index.route('/', methods =['get','POST'])
def show():
    user_id = session.get('user_id')
    userSession = User.query.filter_by(id=user_id).first()
    company_id = session['company_id']
    sessionCompany = Company.query.filter_by(id=company_id).first()
    if auth("/"):
        user_id = session['user_id']
        userSession = User.query.filter_by(id=user_id).first()
        return render_template('index.html',userSession = userSession,user="none", auth=auth, sessionCompany=sessionCompany)
    else:
        return render_template('login.html')