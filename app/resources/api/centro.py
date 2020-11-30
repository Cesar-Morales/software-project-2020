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
from app.helpers.check_api_data import check_data_centro
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
    centros = Centro.getAllAceptados().paginate(pagina, per_page, False)
    total = len(centros.items)

    #Donde se va a formar el json
    data = []
    centro_schema = CentroSchema()

    #Armar la lista para convertirla a json
    for centro in centros.items:
        data.append(centro_schema.dump(centro))

    return jsonify(centros=data, total=total, pagina=pagina), 200

def print_centro(centro):

    #Donde se va a formar el json
    data = []

    #Agregar el centro a data creando el schema
    centro_schema = CentroSchema()
    data.append(centro_schema.dump(centro))

    return jsonify(atributos=data), 200


def show(centro_id):
    """ Endpoint para devolver un centro en particular segun id"""

    #Obtner el centro segun id
    centro = Centro.getCentroAceptado(centro_id)

    if centro:   
        return print_centro(centro)  
    else:
        return jsonify({"error_message": "Not found"}), 404


def create():
    """ Endpoint para crear un centro """

    data = request.get_json(silent=True)

    if check_data_centro(data):
        #Crear centro si no existe
        centro = Centro.createAPI(data)

        #Cheuqear si se pudo crear
        if centro:
            return print_centro(centro)
    else:
        return jsonify({"error_message": "Bad request"}), 400
