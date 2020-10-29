"""
Reservas de centros
"""
from app import db


class Reserva(db.Model):

    id = db.Column(db.Integer, primary_key=True, 
                   nullable=False, 
                   autoincrement=True)
    start_time = db.Column(db.String(80), nullable=False)
    final_time = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), default='')
    phone_number = db.Column(db.String(50), nullable=False)

    centro_id = db.Column(db.Integer, 
                          db.ForeignKey('centro.id'),
                          nullable=False)

    def reservado(form):
        start_time = form.get('hora_inicio')
        date = form.get('fecha')
        center_id = int(form.get('centro_id'))

        # Primero se revisa que el horario para la fecha no exista
        turno = db.session.query(Reserva).filter_by(
                start_time=start_time,
                date=date,
                centro_id=center_id
                ).first()
        return turno

    def create(form):
        if Reserva.reservado(form):
            return False
        else:
            reserva = Reserva(
                    start_time=form.get('hora_inicio'), 
                    final_time=form.get('hora_fin'), 
                    email=form.get('email_donante'), 
                    phone_number=form.get('telefono_donante'), 
                    date=form.get('fecha'), 
                    centro_id=form.get('centro_id'))
            db.session.add(reserva)
            db.session.commit()
            return True


