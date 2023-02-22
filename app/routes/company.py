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
        return render_template('login.html')
    if companies == None:
        return redirect('company.register')
    return render_template('/company/index.html', user=None, auth=auth, companies = companies, userSession=userSession)

@company_bp.route('/company/register', methods=['GET'])
def registerIndex():
    userSessionId = session.get('user_id')
    userSession = User.query.filter_by(id=userSessionId).first()
    if not auth("/company/register"):
        return render_template('login.html')
    return render_template('/company/register.html', auth = auth, userSession = userSession)

