"""
Turnos creados por operator para que luego en la app publica seleccionen
"""
from app import db
from sqlalchemy import asc
from datetime import time, timedelta, date, datetime

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
                date=date.strftime("%Y-%m-%d"),
                centro_id=center_id).first()
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
        final_time = Turno.crearHorarioDeFinalizacion(form.start_time.data)

        if turno:
            # El turno ya existe
            return False
        else:
            # Se crea el nuevo turno
            turno = Turno(centro_id=int(form.center_id.data),
                          start_time=form.start_time.data.strftime("%H:%M:%S"),
                          final_time=final_time.strftime("%H:%M:%S"),
                          date=form.date.data.strftime("%Y-%m-%d"))
            db.session.add(turno)
            db.session.commit()
            return True


    def getTurnosByDate(centro_id):
        dos_dias_futuro = date.today() + timedelta(days=2)
        turnos = Turno.query.filter(
            (Turno.date >= date.today().strftime("%Y-%m-%d")) & 
            (Turno.date <= dos_dias_futuro.strftime("%Y-%m-%d")) & 
            (Turno.centro_id == centro_id) &
            (Turno.selected == False))
        return turnos.order_by(asc(Turno.date)).order_by(asc(Turno.start_time))


    def buscarTurnoPorId(id):
        return db.session.query(Turno).filter_by(id=id).first()

    def update(form, id):
        """ Creción del turno para un centro específico """
        # Datos recibidos del formulario
        turno = Turno.buscarTurno(form)
        # Creacion del horario de finalización
        final_time = Turno.crearHorarioDeFinalizacion(form.start_time.data)
        if turno:
            # El turno ya existe
            return False
        else:
            # Una vez que sabemos que no existe la data para el 
            # centro nos lo traemos y lo modificamos
            turno = Turno.buscarTurnoPorId(id)
            turno.start_time = form.start_time.data.strftime("%H:%M:%S")
            turno.final_time = final_time.strftime("%H:%M:%S")
            turno.date = form.date.data.strftime("%Y-%m-%d")
            db.session.commit()
            return True


    def trash(id):
        """Metodo que recibe un id de turno a borrar"""
        turno = db.session.query(Turno).filter_by(id=id).first()
        db.session.delete(turno)
        db.session.commit()
