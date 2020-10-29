from flask import jsonify
from app.models.centro import Centro
from app.models.turno import Turno
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
    turnos = Centro.getAllTurnosByDate(id)
    data = []

    #Armar la lista para convertirla a json
    for turno in turnos:
        if turno.date == search_date.strftime("%Y-%m-%d"):
            data.append(
                {"centro_id": turno.centro_id, 
                "hora_inicio": turno.start_time, 
                "hora_fin": turno.final_time, 
                "fecha": turno.date}
            )

    return jsonify(turnos=data)