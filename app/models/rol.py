from app import db
from app.models.usuario_tiene_rol import usuario_tiene_rol


class Rol(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    users = db.relationship('User', secondary=usuario_tiene_rol, back_populates='roles')


