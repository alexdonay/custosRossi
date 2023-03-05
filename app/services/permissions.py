from flask import request
from flask_principal import Principal, Permission, RoleNeed, identity_loaded
from app.models import User
from app import app
import app.config as config

principal = Principal(app)

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if hasattr(identity, 'user') and identity.user.is_authenticated:
        role = RoleNeed(identity.user.profile)
        identity.provides.add(role)

        for route, roles in config.PERMISSIONS.items():
            if request.path.startswith(route):
                for role in roles:
                    identity.provides.add(RoleNeed(role))
                break
