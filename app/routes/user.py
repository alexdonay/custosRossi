from flask import (Blueprint, redirect, render_template, request, session,url_for)
from app import db
from app.config import USER_ROLES as roles
from app.models.User import User
from app.services.auth import auth
from app.models.Salary import Salary
import bcrypt
from flask_login import login_required
from datetime import datetime
user_bp = Blueprint('user', __name__)


@user_bp.route('/user/', methods=['GET'])
@login_required
def index(message=""):
    if not auth('/user/'):
        return render_template('notFound.html')

    users = User.query.all()
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()

    return render_template(
        '/users/index.html',
        users=users,
        userSession=userSession,
        auth=auth,
        message=message
    )


@user_bp.route('/user/register', methods=['GET'])
@login_required
def registerIndex():
    if not auth('/user/register/'):
        return render_template('notFound.html')
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()

    return render_template(
        '/users/register.html',
        roles=roles,
        auth=auth,
        userSession=userSession
    )


@user_bp.route('/user/register', methods=['POST'])
@login_required
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
            auth=auth,
            userSession=userSession
        )

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    new_user = User(username=username, password=hashed, profile=profile, name=name)
    
    db.session.add(new_user)
    db.session.commit()
       
    vigenciaInicial = datetime.strptime(request.form.get("vigenciaInicial"), '%Y-%m-%d').date()

    salarioInicial = request.form.get("salarioInicial")
    
    print(f'o usuário: {new_user.id}, o salário: {salarioInicial}') 
    salary = Salary(salary=salarioInicial, start_date=vigenciaInicial, user_id=new_user.id)
    db.session.add(salary)
    db.session.commit()
    
    return redirect('/user')


@user_bp.route('/user/update/<int:user_id>', methods=['GET'])
@login_required
def update(user_id):
    print("chegou")
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    user = User.query.filter_by(id=user_id).first()
    return render_template('/users/update.html', auth=auth, roles=roles, userSession=userSession, user=user)


@user_bp.route('/user/update/<int:user_id>', methods=['POST'])
@login_required
def update_Post(user_id):
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
                userSession=userSession
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


@user_bp.route('/user/delete/<int:user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    if not auth('/user/delete/'):
        return render_template('notFound.html')
    else:
        user = User.query.filter_by(id=user_id).first()
        if user and user_id != session.get('user_id'):
            db.session.delete(user)
            db.session.commit()
            return redirect('/user')
        else:
            userSessionId = session.get('user_id')
            userSession = User.query.filter_by(id=userSessionId).first()
            users = User.query.all()
            return redirect('/user/')

@user_bp.route('/user/salary/<int:user_id>',methods=['GET'])
@login_required
def salary_history(user_id):
    if not auth('/user/salary/'):
        return render_template('notFound.html')
    else:
        user = User.query.get(user_id)
        salaries = Salary.query.filter_by(user_id=user_id).order_by(Salary.start_date.desc()).all()
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        return render_template('/users/salary.html', user=user, salaries=salaries, auth = auth, userSession = userSession)
    
@user_bp.route('/user/salary/new/<int:user_id>', methods=['GET', 'POST'])
@login_required
def addSalary(user_id):
    if not auth('/user/salary/'):
        return render_template('notFound.html')
    else:
        user = User.query.get(user_id)
        if request.method == 'POST':
            salary = request.form.get('salary')
            start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
            salary = Salary(
                salary=salary,
                start_date=start_date,
                user_id=user.id
            )
            db.session.add(salary)
            db.session.commit()
            return redirect(url_for('user.salary', user_id=user.id))
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        return render_template('/users/addSalary.html', user=user, auth=auth, userSession = userSession)