from flask import *
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.models.User import User
from app.services.auth import auth
from app.models.Company import Company
from app import db
login = Blueprint('login', __name__,)
@login.route('/login/', methods=['GET'])
def loginGet():
    companys = Company.query.all()
    return render_template('login.html', companys=companys)

@login.route('/login/', methods=['POST'])
def loginPost():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password) and request.form['companySession'] !="":
        sessionCompany = Company.query.filter_by(id=request.form['companySession']).first()
        session['user_id'] = user.id
        userSession = User.query.filter_by(id=user.id).first()
        return render_template('index.html', userSession = userSession, auth=auth, sessionCompany= sessionCompany)
    else:
        return render_template('login.html', message = "Usuário e senha incorretos ou a empresa não está selecionada")

@login.route('/logout/')
def logout():
    session.pop('user_id', None)
    return redirect('/login')