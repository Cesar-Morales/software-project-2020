from datetime import date, time, timedelta
from app.helpers.forms import TurnoAPIForm


def checkData(form_request, id):
    """ Chequea que los datos de crear reserva sean correctos """

    #Chequear que el id del centro sea el mismo que el parametro
    if id != form_request.get('centro_id'):
        return False

    #Hacer la validaciones de los tiempos
    form = TurnoAPIForm(form_request)

    if not form.validate():
        return False
    
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
        return False
    else:
        return True
    
    