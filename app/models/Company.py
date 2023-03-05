from app import db  

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    social_name = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    street = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(6), nullable=False)
    neighborhood = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80),nullable=True)
    state =db.Column(db.String(80), nullable=True)
    postal_code = db.Column(db.String(8), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    def __init__(self, social_name, cnpj, street, number, neighborhood, postal_code, city,state, phone):
        self.social_name = social_name
        self.cnpj = cnpj
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.phone = phone

    def __repr__(self):
        return f'<Company id:{self.id} social_name:{self.social_name} cnpj:{self.cnpj} street:{self.street} number:{self.number} neighborhood:{self.neighborhood} postal_code:{self.postal_code}>'