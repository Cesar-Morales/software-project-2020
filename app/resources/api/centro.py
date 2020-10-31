""" 
API Centros

Guardo este pedaso de codigo por las dudas
data.append(
            {"nombre": centro.name, 
            "direccion": centro.location,  
            "telefono": centro.phone_number,  
            "hora_apertura": centro.start_time, 
            "hora_cierre": centro.final_time, 
            "tipo": centro.tipo.name, 
            "web": centro.web, 
            "email": centro.email}
        ) 
"""


from flask import jsonify
from flask import request
from app.models.centro import Centro, CentroSchema
from app.models.reseva import Reserva
from flask import request
from datetime import date
from app.models.site import Site
from app.models.turno import Turno
import math

def index():
    """ Endpoint para devolver todos los centros pagianados
    segun el sistema"""

    #Pagina por defecto en caso de no proveer una
    pagina = 1

    #Obtener la pagina si viene como parametro
    if request.args.get('pagina'):
        pagina = int(request.args.get('pagina'))

    #Obtner los centros y paginarlos
    per_page = Site.page()
    #total = Centro.getAll().count()
    centros = Centro.getAll().paginate(pagina, per_page, False)
    total = len(centros.items)

    #Donde se va a formar el json
    data = []
    centro_schema = CentroSchema()

    #Armar la lista para convertirla a json
    for centro in centros.items:
        
        
        data.append(centro_schema.dump(centro))

        

    return jsonify(centros=data, total=total, pagina=pagina), 200

def show(centro_id):
    """ Endpoint para devolver un centro en particular segun id"""

    #Obtner el centro segun id
    centro = Centro.getCentro(centro_id)

    #Donde se va a formar el json
    data = []

    #Agregar el centro a data creando el schema
    centro_schema = CentroSchema()
    data.append(centro_schema.dump(centro))

        

    return jsonify(atributos=data), 200

def create():
    """ Endpoint para crear un centro """

    #Crear la reserva del turno
    if Reserva.create(request.form):

        #Crear el json a devolver
        data = []

        #Armar la lista para convertirla a json
        data.append(
            {"centro_id": request.form.get('centro_id'),
            "email_donante": request.form.get('email_donante'),
            "telefono_donante": request.form.get('telefono_donante'), 
            "hora_inicio": request.form.get('hora_inicio'), 
            "hora_fin": request.form.get('hora_fin'), 
            "fecha": request.form.get('fecha')}
        )

        return jsonify(atributos=data), 201
    else:
        return jsonify({"error_message": "horario ya reservado"}), 404
