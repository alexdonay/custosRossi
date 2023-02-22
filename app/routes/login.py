from flask import *
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.models.User import User
from app.services.auth import auth

login = Blueprint('login', __name__,)
@login.route('/login/', methods=['GET'])
def loginGet():
    return render_template('login.html')

@login.route('/login/', methods=['POST'])
def loginPost():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        session['user_id'] = user.id
        userSession = User.query.filter_by(id=user.id).first()
        return render_template('index.html', userSession = userSession, auth=auth)
    else:
        return render_template('login.html')

@login.route('/logout/')
def logout():
    session.pop('user_id', None)
    return redirect('/login')