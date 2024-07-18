"""
Clase Perros.
"""
from db import db


class Perros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    raza = db.Column(db.String(), nullable=True)
    edad = db.Column(db.Integer(), nullable=True)
    peso = db.Column(db.Float(), nullable=True)
