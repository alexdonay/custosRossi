from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app.config as config
from flask_migrate import Migrate
app = Flask(__name__, static_folder=config.STATIC_FOLDER, template_folder=config.TEMPLATES_FOLDER)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app.routes.index import index
from app.routes.login import login
from app.routes.user import user
from app.routes.company import company_bp 
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(user)
app.register_blueprint(company_bp)




if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
