from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    description = db.Column(db.String(11), nullable=True)
    number = db.Column(db.String(50), nullable=True)
    street = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    users = db.relationship('User', secondary='project_users', backref='projects')
    
    def __init__(self):
        pass

project_users = db.Table('project_users',
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)
