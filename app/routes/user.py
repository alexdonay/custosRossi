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

@user.route('/user/register', methods=['GET', 'POST'])
def register():
    user = session.get('user_id')
    if request.method == 'POST':
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
                user = user

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

    if not auth('/user/register'):
        return render_template('notFound.html')

    
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()

    return render_template(
        '/users/register.html',
        roles=roles,
        auth=auth,
        user=user
    )

@user.route('/user/', methods=['GET'])
def index(message = ""):
    if not auth('/user'):
        return render_template('notFound.html')

    users = User.query.all()
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()

    return render_template(
        '/users/index.html',
        users=users,
        user=user,
        auth=auth,
        message = message
    )

@user.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    user_id = session.get('user_id')
    if user and user_id != user.id:
        db.session.delete(user)
        db.session.commit()
        return redirect('/user')
    else:
        message = "O usuário não existe ou está em uso e não pode ser excluído"
        users = User.query.all()
        return redirect('/user')

@user.route('/alter_user/<int:user_id>', methods=['POST'])
def alter_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        if request.method == 'POST':
            password = request.form['password']
            confirm_password = request.form['confirmPassword']
            if password != confirm_password:
                message = 'As senhas informadas não conferem'
                return render_template(
                    '/users/alter.html',
                    message=message,
                    roles=roles,
                    auth=auth,
                    user=user
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
    else:
        return redirect('/user')