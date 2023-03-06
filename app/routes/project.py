from flask import request, render_template, redirect, url_for, flash, Blueprint, session
from flask_login import login_required
from app import db
from app.models.Project import Project
from app.models.User import User
from app.models.Company import Company
from app.models.Client import Client
from app.services.auth import auth

project_bp = Blueprint('project', __name__)


@project_bp.route('/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'GET':
        users = User.query.all()
        companies = Company.query.all()
        clients = Client.query.all()
        userSession = User.query.get(session.get('user_id'))
        return render_template('/projects/register.html',auth=auth, users=users, companies=companies, clients=clients, userSession = userSession)
    elif request.method == 'POST':
        company_id = request.form['company_id']
        client_id = request.form['client_id']
        description = request.form['description']
        number = request.form['number']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone = request.form['phone']
        user_ids = request.values.getlist('user_ids[]')
        project = Project(company_id=company_id, client_id=client_id, description=description, number=number, street=street, city=city, state=state, zip_code=zip_code, phone=phone)
        for user_id in user_ids:
            user = User.query.filter_by(id=user_id).first()
            project.users.append(user)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('project.index', project_id=project.id))


@project_bp.route('/project')
@login_required
def index():
    userSession = User.query.get(session.get('user_id'))
    projects = Project.query.all()
    print(projects[0].users[0].name)
    return render_template('/projects/index.html', auth=auth, projects=projects, userSession=userSession)
