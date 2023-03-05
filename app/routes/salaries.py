from flask import render_template, redirect, url_for, request, Blueprint,session
from app import db
from app.models.Salary import Salary
from app.services.auth import auth
from flask_login import login_required
from app.models.User import User
salary_bp = Blueprint('salary', __name__)

@salary_bp.route('/salary/', methods=['GET'])
@login_required
def index():
    if auth('/salary/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        salary = Salary.query.all()
        return render_template('salary/index.html', salary=salary, auth = auth,userSession = userSession)
    else:
        return render_template('notFound.html')
    
@salary_bp.route('/salary/register/', methods=['GET'])
@login_required
def register():
    if auth('/salary/register/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        salary = Salary.query.all()
        return render_template('client/register.html', salary, auth = auth,userSession = userSession)
    
    else:
        return render_template('notFound.html')
    
@salary_bp.route('/salary/register/', methods=['POST'])
@login_required
def registerPost():
    if auth('/salary/register/'):

        #adcionar os campo para gerar
        db.session.add()
        db.session.commit()
        return redirect(url_for('client.index'))
    else:
        return render_template('notFound.html')  
