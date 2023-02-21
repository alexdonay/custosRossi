from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db  
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile = db.Column(db.String(80), nullable=False)
    def __init__(self, name, username, password, profile):
        self.name = name
        self.username = username
        self.password = password
        self.profile = profile