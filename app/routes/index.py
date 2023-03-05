from flask import *
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
index_bp = Blueprint('index', __name__)
@index_bp.route('/', methods =['get','POST'])
def show():
       
    return render_template('index.html',userSession = "userSession",user="none", auth=auth)
    