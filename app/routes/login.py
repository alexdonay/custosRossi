from flask import *
from app import db
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.models.User import User
from app.services.auth import auth
from app.models.Company import Company
from flask_login import login_user, logout_user, current_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login/', methods=['GET'])
def loginGet():
    if (User.query.all()==[]):
        userSession = session.get('user_id')
        username = 'admin'
        password = 'admin'
        profile = 'admin'
        name = 'admin'
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        new_user = User( username=username, password=hashed, profile=profile,name=name)
        db.session.add(new_user)
        db.session.commit()
    return render_template('login.html')

@login_bp.route('/login/', methods=['POST'])
def loginPost():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        login_user(user)
        
        session['user_id'] = user.id
        session['profile'] = user.profile
        userSession = User.query.filter_by(id=user.id).first()
        return render_template('index.html', userSession=userSession, auth=auth)
    else:
        return render_template('login.html', message="Usuário e senha incorretos")

@login_bp.route('/logout/')
def logout():
    logout_user()
    session['profile'] = ''
    session['user_id'] = ''
    return redirect('/login')