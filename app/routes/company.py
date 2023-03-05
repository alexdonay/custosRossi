from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
from app import db
company_bp = Blueprint('company', __name__)

@company_bp.route('/company', methods=['GET'])
def index():
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    companies = Company.query.all()
    if not auth("/company"):
        return render_template('notFound.html')
    if companies == None:
        return redirect('company.register')
    return render_template('/company/index.html', user=None, auth=auth, companies = companies, userSession=userSession)

@company_bp.route('/company/register', methods=['GET'])
def registerIndex():
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    if not auth("/company/register"):
        return render_template('notFound.html')
    return render_template('/company/register.html', auth = auth, userSession = userSession)

@company_bp.route('/company/register', methods=['POST'])
def register():
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    if not auth("/company/register"):
        return render_template('notFound.html')
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

@company_bp.route('/company/details/<int:companyId>', methods=['GET'])
def details(companyId):
    if not auth('/company/details/'):
        return render_template('notFound.html')
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    company = Company.query.filter_by(id=companyId).first()
    
    return render_template('/company/details.html', company=company, auth = auth, userSession = userSession)

@company_bp.route('/company/delete/<int:companyId>', methods=['GET'])
def delete(companyId):
    if not auth('/company/delete/'):
        return render_template('notFound.html')
    company = Company.query.filter_by(id=companyId).first()
    db.session.delete(company)
    db.session.commit()
    return redirect('/company')
    
    