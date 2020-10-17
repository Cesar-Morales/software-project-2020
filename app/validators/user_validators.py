from flask_login import current_user


def check_permission(permiso):
    """Controla que el usuario actual tenga un rol que tenga el permiso solicitado"""
    actual_roles = current_user.roles
    actual_permission = []
    for actual_rol in actual_roles:
        for actual_permiso in actual_rol.permisos:
            actual_permission.append(actual_permiso)
    return any(permisotemp.name
               == permiso for permisotemp in actual_permission)
