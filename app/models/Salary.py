from app import db
from datetime import datetime

class Salary(db.Model):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    
    
    
    def __init__(self, user_id, salary, start_date):
        self.user_id = user_id
        self.salary = salary
        self.start_date = start_date
        
    @classmethod
    def get_salary(cls, employee_id, date_ref):
        return cls.query.filter_by(employee_id=employee_id)\
                       .filter(cls.start_date <= date_ref)\
                       .order_by(cls.start_date.desc())\
                       .first()

