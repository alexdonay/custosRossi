from flask import *
from app.models.User import User
from app.services.auth import auth
index = Blueprint('index', __name__)
@index.route('/', methods =['get','POST'])
def show():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    if auth("/"):
        return render_template('index.html',user = user, auth=auth)
    else:
        return render_template('login.html')