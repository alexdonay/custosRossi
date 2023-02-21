from flask import *
from flask_sqlalchemy import SQLAlchemy
from app.models.User import User
import app.config as config
def auth(route):
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return False

    profile = user.profile
    globalPermissions = config.PERMISSIONS
    if profile in globalPermissions[route]:
        return True
    else:
       return False