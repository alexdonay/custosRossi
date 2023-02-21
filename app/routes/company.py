from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models.User import User
from app.models.Company import Company
from app.services.auth import auth
from app import db
company_bp = Blueprint('company', __name__)

@company_bp.route('/company', methods=['GET'])
def index():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    companyes = User.query.all()
    if not auth("/company"):
        return render_template('login.html')
    if companyes == None:
        return redirect('company.register')
    return render_template('/company/index.html',user=user, auth=auth, company = None)

@company_bp.route('/company/register', methods=['GET'])
def register():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    if not auth("/company"):
        return render_template('login.html')

    return render_template('index.html',user=user, auth=auth)