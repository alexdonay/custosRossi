from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile = db.Column(db.String(80), nullable=False)
    salaries = db.relationship('Salary', backref='user', lazy=True)

    def __init__(self, name, username, password, profile):
        self.name = name
        self.username = username
        self.password = password
        self.profile = profile

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
  
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def set_profile(self, profile):
        self.profile = profile
        db.session.add(self)
        db.session.commit()