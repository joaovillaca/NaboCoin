from flask_sqlalchemy import SQLAlchemy
from application import app

database = SQLAlchemy(app)

class Usuario(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(60), unique=True, nullable=False)
    email = database.Column(database.String(60), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    carteira = database.relationship('Carteira', backref=database.backref('user', lazy=True), uselist=False, nullable=False)

class Carteira(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    saldoNabo = database.Column(database.Float)
    saldoReais = database.Column(database.Float)
    

