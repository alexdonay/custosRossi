from flask import Blueprint, render_template, request, session, redirect
from flask_login import login_required
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
from app import db
import re
company_bp = Blueprint('company', __name__)

@company_bp.route('/company/', methods=['GET'])
@login_required
def index():
    if auth('/company/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        companies = Company.query.all()
        if companies == None:
            return redirect('company.register')
        return render_template('/company/index.html', user=None, auth=auth, companies = companies, userSession=userSession)
    else:
        return render_template('notFound.html')
@company_bp.route('/company/register/', methods=['GET'])
@login_required
def registerIndex():
    if auth('/company/register/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        return render_template('/company/register.html', auth = auth, userSession = userSession)
    else:
        return render_template('notFound.html')
@company_bp.route('/company/register/', methods=['POST'])
@login_required
def register():
    if auth('/company/register/'):
        company = Company(
            social_name = request.form['social_name'],
            cnpj = request.form['cnpj'],
            street = request.form['street'],
            number = request.form['number'],
            neighborhood = request.form['neighborhood'],
            postal_code = request.form['postal_code'],
            city = request.form['city'],
            state = request.form['state'],
            phone = request.form['phone']
        )
        db.session.add(company)
        db.session.commit()
        return redirect('/company')
    else:
        return render_template('notFound.html')
    
@company_bp.route('/company/details/<int:companyId>', methods=['GET'])
@login_required
def details(companyId):
    if auth('/company/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        company = Company.query.filter_by(id=companyId).first()
        return render_template('/company/details.html', company=company, auth = auth, userSession = userSession)
    else:
        return render_template('notFound.html')
    
@company_bp.route('/company/delete/<int:companyId>', methods=['GET'])
@login_required
def delete(companyId):
    if auth('/company/delete/'):
        company = Company.query.filter_by(id=companyId).first()
        db.session.delete(company)
        db.session.commit()
        return redirect('/company')
    else:
        return render_template('notFound.html')
        
@company_bp.route('/company/update/<int:companyId>', methods=['GET'])
@login_required
def update(companyId):
    if auth('/company/delete/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        company = Company.query.filter_by(id=companyId).first()
        return render_template('/company/update.html', company=company, auth = auth, userSession = userSession)
    else:
        return render_template('notFound.html')
    

@company_bp.route('/company/update/<int:companyId>', methods=['POST'])
@login_required
def updatePost(companyId):
    if auth('/company/update/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        company = Company.query.filter_by(id=companyId).first()
        company.social_name = request.form['social_name']
        company.cnpj =re.sub(r'\D', '', request.form['cnpj'])
        company.street = request.form['street']
        company.number = request.form['number']
        company.neighborhood = request.form['neighborhood']
        company.postal_code = re.sub(r'\D', '',request.form['postal_code'])
        company.city = request.form['city']
        company.state = request.form['state']
        company.phone = re.sub(r'\D', '',request.form['phone'])
        db.session.add(company)
        db.session.commit()

        return redirect('/company')
    else:
        return render_template('notFound.html')