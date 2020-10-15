from app import db
from app.models.permiso import Permiso
from app.models.rol import Rol
from app.models.user import User
def check_permission(permiso):
    actual_roles = current_user.roles
    actual_permision = []
    for actual_rol in actual_roles:
        actual_permission.append(actual_rol.permisos)
    return any(permisotemp == permiso for permisotemp in actual_permission)