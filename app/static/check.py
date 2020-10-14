from app import db, session
from app.models.permiso import Permiso
from app.models.rol import Rol

def tiene_permiso(permiso):
    permiso_db = db.session.query(Permiso).filter_by(name = permiso).first()
    for rol in session[roles]:
        rol_db = db.session.query(Rol).filter_by(name = rol)
        for permisos in rol_db.permisos:
            