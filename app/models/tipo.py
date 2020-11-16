"""
Modelo de tipos de centros de ayuda
"""
from app import db

class Tipo(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    centros = db.relationship('Centro', backref='tipo', lazy='dynamic')

    def searchById(id):
        return db.session.query(Tipo).filter_by(id=id).first()

    def searchByName(name):
        return db.session.query(Tipo).filter_by(name=name).first()

    def getAllTypes():
        return db.session.query(Tipo).all()    

    