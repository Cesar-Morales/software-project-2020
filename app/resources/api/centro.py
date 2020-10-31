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

    #Obtner los turnos los centros y paginarlo
    per_page = Site.page()
    #total = Centro.getAll().count()
    centros = Centro.getAll().paginate(pagina, per_page, False)
    total = len(centros.items)

    #Donde se va a formar el jason
    data = []
    centro_schema = CentroSchema()

    #Armar la lista para convertirla a json
    for centro in centros.items:
        
        
        data.append(centro_schema.dump(centro))

        

    return jsonify(centros=data, total=total, pagina=pagina), 200
