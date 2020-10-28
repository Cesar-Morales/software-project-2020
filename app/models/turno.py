"""
Turnos creados por operator para que luego en la app publica seleccionen
"""
from app import db
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


    def buscarTurno(form):
        start_time = form.start_time.data
        date = form.date.data
        center_id = int(form.center_id.data)

        # Primero se revisa que el horario para la fecha no exista
        turno = db.session.query(Turno).filter_by(
                start_time=start_time.strftime("%H:%M:%S"),
                date=date.strftime("%d/%m/%y"),
                center_id=center_id).first()
        return turno

    def crearHorarioDeFinalizacion(start_time):
        deltatime = timedelta(minutes=30)
        aux_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
        aux_time = aux_time + deltatime
        hours = aux_time.seconds // 3600
        minutes = (aux_time.seconds // 60) % 60
        final_time = time(hours, minutes)
        return final_time

    def create(form):
        """ Creción del turno para un centro específico """
        # Datos recibidos del formulario
        turno = Turno.buscarTurno(form)
        # Creacion del horario de finalización
        final_time = Turno.crearHorarioDeFinalizacion(form.start_time)

        if turno:
            # El turno ya existe
            return False
        else:
            # Se crea el nuevo turno
            turno = Turno(centro_id=form.center_id,
                          start_time=form.start_time.strftime("%H:%M:%S"),
                          final_time=final_time.strftime("%H:%M:%S"),
                          date=form.date.strftime("%d/%m/%y"))
            db.session.add(turno)
            db.session.commit()
            return True

    def update(form):
        """ Creción del turno para un centro específico """
        # Datos recibidos del formulario
        turno = Turno.buscarTurno(form)
        # Creacion del horario de finalización
        final_time = Turno.crearHorarioDeFinalizacion(form.start_time)
        if turno:
            # El turno ya existe
            return False
        else:
            # Se crea el nuevo turno
            turno.start_time = form.start_time.strftime("%H:%M:%S")
            turno.final_time = final_time.strftime("%H:%M:%S")
            turno.date = form.date.strftime("%d/%m/%y")
            db.session.commit()
            return True


    def trash(id):
        """Metodo que recibe un id de turno a borrar"""
        turno = db.session.query(Turno).filter(id=id).first()
        db.session.delete(turno)
        db.session.commit()
