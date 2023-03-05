from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app.config as config
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, static_folder=config.STATIC_FOLDER, template_folder=config.TEMPLATES_FOLDER)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['PRINCIPAL_PERMISSIONS'] = config.PERMISSIONS
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)

from app.routes.index import index_bp
from app.routes.login import login_bp
from app.routes.user import user_bp
from app.routes.company import company_bp 
from app.routes.client import client_bp
from app.routes.salaries import salary_bp
from app.routes.project import project_bp
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(user_bp)
app.register_blueprint(company_bp)
app.register_blueprint(client_bp)
app.register_blueprint(salary_bp)
app.register_blueprint(project_bp)