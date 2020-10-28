"""
Turnos creados por operator para que luego en la app publica seleccionen
"""
from app import db
from app.helpers.forms import TurnoForm
from datetime import time, timedelta

class Turno(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    start_time = db.Column(db.String(80), nullable=False)
    final_time = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    selected = db.Column(db.Boolean, default=False)

    centro_id = db.Column(db.Integer, 
                          db.ForeignKey('centro.id'),
                          nullable=False)

    def create(form):
        """ Creción del turno para un centro específico """
        #Datos recibidos del formulario
        start_time = form.start_time.data
        date = form.date.data
        center_id = int(form.center_id.data)
        
        #Creacion del horario de finalización
        deltatime = timedelta(minutes=30)
        aux_time = timedelta(hours= start_time.hour, minutes=start_time.minute)
        aux_time = aux_time + deltatime
        hours = aux_time.seconds // 3600
        minutes = (aux_time.seconds // 60)%60
        final_time = time(hours,minutes)

        #Primero se revisa que el horario para la fecha no exista
        turno = db.session.query(Turno).filter_by(
                start_time=start_time.strftime("%H:%M:%S"), 
                date=date.strftime("%d/%m/%y")).first()

        if turno:
            #El turno ya existe
            return False
        else:
            #Se crea el nuevo turno
            turno = Turno(centro_id=center_id, 
                          start_time=start_time.strftime("%H:%M:%S"), 
                          final_time=final_time.strftime("%H:%M:%S"), 
                          date=date.strftime("%d/%m/%y"))
            db.session.add(turno)
            db.session.commit()
            return True




    
