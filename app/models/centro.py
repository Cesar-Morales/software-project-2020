"""
Modulo que contra la relacion con la tabla de centros de ayuda
de la base de datos y el manejo de los mismos.
"""
from app import db
from sqlalchemy import or_
from flask import current_app
from werkzeug.utils import secure_filename

class Centro(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(80), nullable=False, default='09:00')
    final_time = db.Column(db.String(80), nullable=False, default='16:00')
    municipality = db.Column(db.String(80), nullable=False)
    web = db.Column(db.String(80), default='')
    email = db.Column(db.String(80), default='')
    pdf_name = db.Column(db.String(100), default='')
    coordinates = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(80), default='pendiente')

    
    tipoId = db.Column(db.Integer, 
                     db.ForeignKey('tipo.id'))
    turnos = db.relationship('Turno', backref='centro', lazy=True)
    reservas = db.relationship('Reserva', backref='centro', lazy=True)
