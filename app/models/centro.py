"""
Modulo que modela la relacion con la tabla de centros de ayuda
de la base de datos y el esquema para poder serializarlos
"""
from app import db, ma
from sqlalchemy import and_
from flask import current_app
from werkzeug.utils import secure_filename
from marshmallow import fields
from app.models.tipo import Tipo
from marshmallow import Schema, fields, pre_load

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
    turnos = db.relationship('Turno', backref='centro', lazy='dynamic')
    reservas = db.relationship('Reserva', backref='centro', lazy='dynamic')

    def getAllTurnosById(id):
        centro = db.session.query(Centro).filter_by(id=id).first()
        return centro.turnos

    def getCentro(id):
        centro = db.session.query(Centro).filter_by(
                                            id=id, 
                                            estado='aceptado').first()
        return centro
        
    def getAll():
        return db.session.query(Centro).filter_by(estado='aceptado')

    def getState(id):
        centro = db.session.query(Centro).filter_by(id=id).first()
        return centro.estado

class CentroSchema(Schema):
    class Meta:
        model = Centro
        ordered = True

    name = fields.Str()
    location = fields.Str()
    phone_number = fields.Str()
    start_time = fields.Str()
    final_time = fields.Str()
    tipo = fields.Pluck("self", "name")
    web = fields.Str()
    email = fields.Str()
