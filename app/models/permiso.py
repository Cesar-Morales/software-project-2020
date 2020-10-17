from app import db
from app.models.rol_tiene_permiso import rol_tiene_permiso

class Permiso(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    roles = db.relationship('Rol', secondary=rol_tiene_permiso, back_populates='permisos')
