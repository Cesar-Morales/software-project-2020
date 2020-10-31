"""
Reservas de centros
"""
from app import db
from app.models.centro import Centro


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

        # Primero se revisa que el horario para la fecha y el centro no exista
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
            centro_buscado = Centro.getCentro(form.get('centro_id'))
            reserva = Reserva(
                    start_time=form.get('hora_inicio'), 
                    final_time=form.get('hora_fin'), 
                    email=form.get('email_donante'), 
                    phone_number=form.get('telefono_donante'), 
                    date=form.get('fecha'), 
                    centro_id=form.get('centro_id'))
            reserva.centro = centro_buscado
            db.session.add(reserva)
            db.session.commit()
            return True

    def getAll():
        return db.session.query(Reserva).all()

    def search(centro_name, user_email):
        if not centro_name and user_email != '':
            reservas = db.session.query(Reserva).filter(Reserva.email == user_email)
        elif user_email == '':
            reservas = db.session.query(Reserva).join(Centro).filter(Centro.name.like('%'+centro_name+'%'))
        else:
            reservas = db.session.query(Reserva).join(Centro).filter((Reserva.email == user_email)
                                                        & (Centro.name.like('%'+centro_name+'%')))
        return reservas
