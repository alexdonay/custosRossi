from flask import render_template, redirect, url_for, request, Blueprint,session
from app import db
from app.models.Client import Client
from app.services.auth import auth
from flask_login import login_required
from app.services.auth import auth
from app.models.User import User
from app.models.Salary import Salary
client_bp = Blueprint('client', __name__)

@client_bp.route('/client/', methods=['GET'])
@login_required
def index():
    if auth('/client/'):
        users = User.query.all()
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        clients = Client.query.all()
        return render_template('client/index.html', clients=clients, auth = auth,userSession = userSession)
    else:
        return render_template('notFound.html')
    
@client_bp.route('/client/register/', methods=['GET'])
@login_required
def register():
    if auth('/client/register/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        clients = Client.query.all()
        return render_template('client/register.html', clients=clients, auth = auth,userSession = userSession)
    
    else:
        return render_template('notFound.html')
    
@client_bp.route('/client/register/', methods=['POST'])
@login_required
def registerPost():
    if auth('/client/register/'):
        social_name = request.form.get('social_name')
        cnpj = request.form.get('cnpj')
        cpf = request.form.get('cpf')
        street = request.form.get('street')
        number = request.form.get('number')
        neighborhood = request.form.get('neighborhood')
        city = request.form.get('city')
        state = request.form.get('state')
        postal_code = request.form.get('postal_code')
        phone = request.form.get('phone')
        observation = request.form.get('observation')
        client = Client(social_name=social_name, cnpj=cnpj, cpf=cpf, street=street, number=number, neighborhood=neighborhood, city=city, state=state, postal_code=postal_code, phone=phone, observation=observation)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('client.index'))
    else:
        return render_template('notFound.html')
    
@client_bp.route('/client/details/<int:clientId>', methods=['GET'])
@login_required
def details(clientId):
    if auth('/client/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        client = Client.query.filter_by(id=clientId).first()
        return render_template('/client/details.html', client=client, auth = auth, userSession = userSession)
    else:
        return render_template('notFound.html')
    
@client_bp.route('/client/update/<int:clientId>', methods=['GET'])
@login_required
def update(clientId):
    if auth('/client/delete/'):
        userSessionId = session.get('user_id')
        userSession = User.query.filter_by(id=userSessionId).first()
        client = Client.query.filter_by(id=clientId).first()
        return render_template('/client/update.html', client=client, auth = auth, userSession = userSession)
    else:
        return render_template('notFound.html')

@client_bp.route('/client/update/<int:clientId>', methods=['POST'])
@login_required
def updatePost(clientId):
    if auth('/client/update/'):
        client = Client.query.filter_by(id=clientId).first()
        client.social_name = request.form['social_name']
        client.cnpj =  request.form['cnpj']
        client.street = request.form['street']
        client.number = request.form['number']
        client.neighborhood = request.form['neighborhood']
        client.postal_code = request.form['postal_code']
        client.city = request.form['city']
        client.state = request.form['state']
        client.phone = request.form['phone']
        client.observation = request.form['observation']
        db.session.add(client)
        db.session.commit()

        return redirect('/client/')
    else:
        return render_template('notFound.html')
   
@client_bp.route('/client/delete/<int:clientId>', methods=['GET'])
@login_required
def delete(clientId):
    if auth('/client/delete/'):
        client = Client.query.filter_by(id=clientId).first()
        db.session.delete(client)
        db.session.commit()
        return redirect('/client')
    else:
        return render_template('notFound.html')
