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
    users = db.relationship('User', secondary='project_users', backref=db.backref('projects', lazy=True))
    
    def __init__(self, company_id, client_id, description, number, street, city, state, zip_code, phone):
        self.company_id = company_id
        self.client_id = client_id
        self.description = description
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

def __repr__(self):
    return f'<Project {self.id}: {self.description} ({self.city}, {self.state}) Company: {self.company.name}, Client: {self.client.name}, Users: {[user.username for user in self.users]}>'
project_users = db.Table('project_users',
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

