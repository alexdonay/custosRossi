from datetime import date
from flask_sqlalchemy import SQLAlchemy
from app import db

class Salary(db.Model):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    def __init__(self, employee_id, salary, start_date, end_date):
        self.employee_id = employee_id
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date