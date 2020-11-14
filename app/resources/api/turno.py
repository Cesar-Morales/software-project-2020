""" API de turnos """

from flask import jsonify
from flask import request
from app.models.centro import Centro
from app.models.reseva import Reserva
from app.helpers.reserva import checkData
from flask import request
from datetime import date

def index(id):
    """ Endpoint para devolver todos los turnos de un centro """

    #Valor por defecto si fecha no existe
    search_date = date.today()

    #Obtener la fecha si viene como parametro
    if request.args.get('fecha'):
        search_date = date.fromisoformat(request.args.get('fecha'))
            

    #Obtner los turnos del centro segun la fecha    
    turnos = Centro.getAllTurnosById(id)
    data = []

    #Armar la lista para convertirla a json
    for turno in turnos:
        if turno.date == search_date.strftime("%Y-%m-%d") and not turno.selected:
            data.append(
                {"centro_id": turno.centro_id, 
                "hora_inicio": turno.start_time, 
                "hora_fin": turno.final_time, 
                "fecha": turno.date}
            )

    return jsonify(turnos=data), 200

def reserva(id):
    """ Endpoint para reservar un turno. No verifica que sea multiplo 
    de 30 o que el id del centro fue enviado """

    #Crear la reserva del turno
    if (checkData(request.form,id) and
        Reserva.create(request.form)):

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
        return jsonify({"error_message": "error al crear reserva"}), 404