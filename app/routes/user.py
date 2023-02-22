from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
)
from app import db
from app.config import USER_ROLES as roles
from app.models.User import User
from app.services.auth import auth
import bcrypt

user = Blueprint('user', __name__)

@user.route('/user/', methods=['GET'])
def index(message = ""):
    if not auth('/user'):
        return render_template('notFound.html')

    users = User.query.all()
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()

    return render_template(
        '/users/index.html',
        users=users,
        userSession=userSession,
        auth=auth,
        message = message
    )

@user.route('/user/register', methods=['GET'])
def registerIndex():
    if not auth('/user/register'):
        return render_template('notFound.html')
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()

    return render_template(
        '/users/register.html',
        roles=roles,
        auth=auth,
        userSession=userSession
    )

@user.route('/user/register', methods=['POST'])
def register():
    userSession = session.get('user_id')
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    profile = request.form['profile']
    name = request.form['name']

    if password != confirm_password:
        message = 'As senhas informadas não conferem'
        return render_template(
            '/users/register.html',
            message=message,
            roles=roles,
            auth = auth,
            userSession = userSession
            )

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    new_user = User(
        username=username,
        password=hashed,
        profile=profile,
        name=name
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect('/user')

@user.route('/alter_user/<int:user_id>', methods=['GET'])
def alter_userIndex(user_id):
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    user = User.query.filter_by(id=user_id).first()
    return render_template('/users/alter.html',auth = auth, roles = roles, userSession = userSession, user = user)

@user.route('/alter_user/<int:user_id>', methods=['POST'])
def alter_user(user_id):
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    user = User.query.filter_by(id=user_id).first()
    
    if user:
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        if password != confirm_password:
            message = 'As senhas informadas não conferem'
            return render_template(
                '/users/alter.html',
                message=message,
                roles=roles,
                auth=auth,
                user=user,
                userSession = userSession
            )
        else:
            user.name = request.form['name']
            user.username = request.form['username']
            user.profile = request.form['profile']
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            user.password = hashed
            db.session.commit()
            return redirect('/user')
    else:
        return render_template('/users/alter.html', user=user, auth=auth, roles=roles)


@user.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user and user_id != user.id:
        db.session.delete(user)
        db.session.commit()
        return redirect('/user')
    else:
        return redirect('/user')

