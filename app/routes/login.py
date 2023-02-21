from flask import *
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.models.User import User
login = Blueprint('login', __name__,)
@login.route('/login/', methods=['GET'])
def loginGet():
    return render_template('login.html')

@login.route('/login/', methods=['POST'])
def loginPost():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    users = User.query.all()
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        
        session['user_id'] = user.id

        return redirect('/')
    else:
        return render_template('login.html')

@login.route('/logout/')
def logout():
    session.pop('user_id', None)
    return redirect('/login')