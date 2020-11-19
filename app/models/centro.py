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
import os
from geoalchemy2 import Geometry


class Centro(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(80), nullable=False, default='09:00')
    final_time = db.Column(db.String(80), nullable=False, default='16:00')
    municipality = db.Column(db.String(80), default='No especificado')
    web = db.Column(db.String(80), default='')
    email = db.Column(db.String(80), default='')
    pdf_name = db.Column(db.String(100), default='')
    coordinates = db.Column(db.String(80),default='')
    estado = db.Column(db.String(80), default='pendiente')

    tipoId = db.Column(db.Integer, db.ForeignKey('tipo.id'))
    turnos = db.relationship('Turno', backref='centro', lazy='dynamic')
    reservas = db.relationship('Reserva', backref='centro', lazy='dynamic')
    
    def getAll():
        """Metodo que devuelve todos los centros creados en la base de datos: sin filtros"""
        return db.session.query(Centro).all()
    
    def getAllAceptados():
        return db.session.query(Centro).filter_by(estado='aceptado')

    def createAPI(form):
        
        #Almacenar variables obtenidas por parametros
        nombre = form.get('nombre')
        direccion = form.get('direccion')
        telefono = form.get('telefono')
        hora_apertura = form.get('hora_apertura')
        hora_cierre = form.get('hora_cierre')
        web = form.get('web')
        email = form.get('email')

        #Buscar id del tipo de centro
        tipo = Tipo.searchByName(form.get('tipo'))

        nuevo = Centro(name=nombre, 
                       location=direccion, 
                       phone_number=telefono, 
                       start_time=hora_apertura, 
                       final_time=hora_cierre, 
                       web=web, 
                       email=email, 
                       estado='pendiente', 
                       tipoId = tipo.id)
        db.session.add(nuevo)
        db.session.commit()
        
        return nuevo

    def create(requestForm, file):
        nombre = requestForm.nombre.data
        direccion = requestForm.direccion.data
        telefono = requestForm.telefono.data
        hora_apertura = requestForm.hora_apertura.data
        hora_cierre = requestForm.hora_cierre.data
        municipalidad = requestForm.municipalidad.data
        web = requestForm.web.data
        email = requestForm.email.data
        coordenadas = requestForm.coordenadas.data

        #Guardamos el PDF
        if file.filename == '':
            pdf_name = ''
        else:
            pdf_name = file.filename
            pdf_path = os.path.join(current_app.config['UPLOAD_FOLDER'], pdf_name)
            file.save(pdf_path)
        
        #Buscar id del tipo de centro
        tipo = Tipo.searchByName(requestForm.tipo.data)

        nuevo = Centro(email=email, 
                       name=nombre, 
                       location=direccion,
                       start_time=hora_apertura,
                       final_time=hora_cierre, 
                       municipality=municipalidad, 
                       web=web,
                       phone_number=telefono, 
                       pdf_name=pdf_name, 
                       coordinates = coordenadas, 
                       estado='aceptado', 
                       tipoId=tipo.id)
        db.session.add(nuevo)
        db.session.commit()
        return True

    def updateCentro(requestForm, id, file):

        centro = db.session.query(Centro).filter_by(id=id).first()

        nombre = requestForm.nombre.data
        direccion = requestForm.direccion.data
        telefono = requestForm.telefono.data
        hora_apertura = requestForm.hora_apertura.data
        hora_cierre = requestForm.hora_cierre.data
        municipalidad = requestForm.municipalidad.data
        web = requestForm.web.data
        email = requestForm.email.data
        coordenadas = requestForm.coordenadas.data
        
        #Guardamos el PDF
        if file.filename == '':
            pdf_name = requestForm.instrucciones.data
        else:
            pdf_name = file.filename
            pdf_path = os.path.join(current_app.config['UPLOAD_FOLDER'], pdf_name)
            file.save(pdf_path)
        
        #Buscar id del tipo de centro
        tipo = Tipo.searchByName(requestForm.tipo.data)

        centro.email=email
        centro.name=nombre
        centro.location=direccion
        centro.start_time=hora_apertura
        centro.final_time=hora_cierre
        centro.municipality=municipalidad
        centro.web=web
        centro.phone_number=telefono 
        centro.pdf_name=pdf_name 
        centro.coordinates = coordenadas
        centro.estado='aceptado'
        centro.tipoId=tipo.id

        db.session.commit()
        return True    

    def getAllTurnosById(id):
        centro = db.session.query(Centro).filter_by(id=id).first()
        return centro.turnos

    def getCentro(id):
        centro = db.session.query(Centro).filter_by(id=id).first()
        return centro

    def getCentroAceptado(id):
        centro = db.session.query(Centro).filter_by(
                                            id=id, 
                                            estado='aceptado').first()
        return centro    

    def getState(id):
        centro = db.session.query(Centro).filter_by(id=id).first()
        return centro.estado

    def search(centro_name, option):
        if not centro_name and option != '':
            
            centros = db.session.query(Centro).filter(Centro.estado == option)
            
        elif option == '':
            centros = db.session.query(Centro).filter(Centro.name.like('%'+centro_name+'%'))
        else:
             centros = db.session.query(Centro).filter((Centro.estado == option)
                                                        & (Centro.name.like('%'+centro_name+'%')))
            
        return centros 
    
    def accept(requestForm):
        idd = requestForm['id']
        center = db.session.query(Centro).filter(Centro.id == idd).first()
        center.estado = 'aceptado'
        db.session.commit()
        return True

    def trashOrReject(requestForm):
        """Metodo que recibe un id de centro a borrar a traves de un formulario."""
        idCenter = requestForm['id']
        state = requestForm['state']
        center = db.session.query(Centro).filter(Centro.id == idCenter).first()
        #Reviso si el usuario a borrar es un administrador. Si es, devuelvo false para que no puedan borrarlo, si no, lo bloqueo.
        center.estado = state
        db.session.commit()
        return True       


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
