from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
from app import db
company_bp = Blueprint('company', __name__)

@company_bp.route('/company', methods=['GET'])
def index():
    user_id = session.get('user_id')
    companyes = Company.query.all()
    if not auth("/company"):
        return render_template('login.html')
    if companyes == None:
        print(companyes)
        return redirect('company.register')
    company = Company.query.all()
    
    return render_template('/company/index.html',user=None, auth=auth,company = company, id = 1)

@company_bp.route('/company', methods=['POST'])
def register():
    user_id = session.get('user_id')
    if not auth("/company"):
        return render_template('login.html')
    social_name = request.form['social_name']
    cnpj = request.form['cnpj']
    street = request.form['street']
    number = request.form['number']
    neighborhood = request.form['neighborhood']
    postal_code = request.form['postal_code']
        
    company = Company(social_name=social_name, cnpj=cnpj, street=street, number=number, neighborhood=neighborhood, postal_code=postal_code)
    db.session.add(company)
    db.session.commit()
        
    return redirect(url_for('company.index'))
    