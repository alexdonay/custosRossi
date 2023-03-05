from flask import request, render_template, redirect, url_for, flash,Blueprint, session
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
    if request.method == 'POST':
        company_id = request.form.get('company_id')
        client_id = request.form.get('client_id')
        description = request.form.get('description')
        address = request.form.get('address')
        number = request.form.get('number')
        project = Project(
            company_id=company_id,
            client_id=client_id,
            description=description,
            address=address,
            number = number
        )
        db.session.add(project)
        db.session.commit()
        flash('Projeto criado com sucesso!', 'success')

        return redirect(url_for('project'))
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    company = Company.query.all()
    client = Client.query.all()
    return render_template('/projects/register.html', Client = client, Company = company, auth = auth,  userSession = userSession)
    

@project_bp.route('/project')
@login_required
def index():
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    projects = Project.query.all()
    return render_template('/projects/index.html', auth = auth, projects=projects, userSession = userSession)
