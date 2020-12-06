from datetime import date, time, timedelta
from app.helpers.forms import TurnoAPIForm, CenterNewAPIForm
from app.models.tipo import Tipo
from werkzeug.datastructures import ImmutableMultiDict


def check_data_reserva(form_request, id):
    """ Chequea que los datos de crear reserva sean correctos """

    #Chequear que el id del centro sea el mismo que el parametro
    if id != form_request.get('centro_id'):
        return [False, {
            "id": ["El id del url y enviado por parametro no coincide"]}]

    #Hacer la validaciones de los tiempos
    form = TurnoAPIForm(form_request)

    if not form.validate():
        return [False, form.errors]
    
    #Chequear que el tiempo tenga diferencia de 30 minutos
    start_time = time.fromisoformat(form_request.get('hora_inicio'))
    end_time = time.fromisoformat(form_request.get('hora_fin'))
    diferencia =  (
        timedelta(
            hours=end_time.hour, 
            minutes=end_time.minute) - 
        timedelta(
            hours=start_time.hour, 
            minutes=start_time.minute))
    
    if diferencia != timedelta(seconds=1800):
        return [False, {
                    "time": [
                        "La diferencia entre la hora de inicio" + 
                        " y de fin debe ser 30 minutos"]
                }]
    else:
        return [True, form.errors]

def check_data_centro(form_request):

    #Hacer la validaciones de los tiempos
    form = CenterNewAPIForm(form_request)

    if not form.validate():
        return [False, form.errors]
    
    #Chequear que el tipo de centro exista
    if Tipo.searchByName(form_request.get('tipo')):
        return [True, form.errors]
    else:
        return [False, {"tipo": ["El tipo de centro no existe"]}]
    