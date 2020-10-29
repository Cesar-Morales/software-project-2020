""" 
Creacion de la base de datos
"""

from app import db
from app.models.user import User
from app.models.rol import Rol
from app.models.site import Site
from app.models.permiso import Permiso
from sqlalchemy import or_
from app.models.centro import Centro
from app.models.tipo import Tipo
from app.models.turno import Turno
from app.models.reseva import Reserva

db.create_all()
# ----------- Creación de datos inciales para la apliación ----------- 

#Creación del objeto sistio si no existe
site = db.session.query(Site).first()
if not site:
    site_new = Site(
        title='AyudAR', 
        email='ayudar@gmail.ar' , 
        description='Sistema de ayuda social')
    db.session.add(site_new)
    db.session.commit()


#Creacion admin inicial del sistema si no existe
user = db.session.query(User).filter(or_(User.username == 'admin', User.email == 'admin')).first()
if not user:
    user = User(
        email='admin@admin.com', 
        last_name='Marcos', 
        first_name='Carlos', 
        password='123123', 
        username='admin')
    db.session.add(user)
    db.session.commit()
    
#Creacion operator para probar permisos  
user_operator = db.session.query(User).filter(or_(User.username == 'operator', User.email == 'operator')).first()
if not user_operator:
    user_operator = User(
        email = 'operator@operator.com', 
        last_name = 'Maria', 
        first_name = 'Marta', 
        password = '123123', 
        username = 'operator')
    db.session.add(user_operator)
    db.session.commit()

#Creacion de roles
#Crea rol admin si no existe
rol_admin = db.session.query(Rol).filter_by(name='admin').first()
if not rol_admin:
    rol_admin = Rol(name='admin')
    db.session.add(rol_admin)
    db.session.commit()

#Crea rol operador si no existe
rol_operador = db.session.query(Rol).filter_by(name='operador').first()
if not rol_operador:
    rol_operador = Rol(name='operador')
    db.session.add(rol_operador)
    db.session.commit()

#Crea rol user si no existe. Este se usa cuando se crea user por primera vez
rol_user = db.session.query(Rol).filter_by(name='user').first()
if not rol_user:
    rol_user = Rol(name='user')
    db.session.add(rol_user)
    db.session.commit()    


#Crear permisos
#Permisos para modulo config
permiso_config_index = db.session.query(Permiso).filter_by(
    name='config_index'
    ).first()
if not permiso_config_index:
    permiso_config_index = Permiso(name='config_index')
    db.session.add(permiso_config_index)
    db.session.commit()

permiso_config_new = db.session.query(Permiso).filter_by(
    name='config_new'
    ).first()
if not permiso_config_new:
    permiso_config_new = Permiso(name='config_new')
    db.session.add(permiso_config_new)
    db.session.commit()

permiso_config_destroy = db.session.query(Permiso).filter_by(
    name='config_destroy'
    ).first()
if not permiso_config_destroy:
    permiso_config_destroy = Permiso(name='config_destroy')
    db.session.add(permiso_config_destroy)
    db.session.commit()

permiso_config_update = db.session.query(Permiso).filter_by(
    name='config_update'
    ).first()
if not permiso_config_update:
    permiso_config_update = Permiso(name='config_update')
    db.session.add(permiso_config_update)
    db.session.commit()

permiso_config_show = db.session.query(Permiso).filter_by(
    name='config_show'
    ).first()
if not permiso_config_show:
    permiso_config_show = Permiso(name='config_show')
    db.session.add(permiso_config_show)
    db.session.commit()

#Permisos para modulo usuario
permiso_user_index = db.session.query(Permiso).filter_by(
    name='user_index'
    ).first()
if not permiso_user_index:
    permiso_user_index = Permiso(name='user_index')
    db.session.add(permiso_user_index)
    db.session.commit()

permiso_user_new = db.session.query(Permiso).filter_by(
    name='user_new'
    ).first()
if not permiso_user_new:
    permiso_user_new = Permiso(name='user_new')
    db.session.add(permiso_user_new)
    db.session.commit()

permiso_user_destroy = db.session.query(Permiso).filter_by(
    name='user_destroy'
    ).first()
if not permiso_user_destroy:
    permiso_user_destroy = Permiso(name='user_destroy')
    db.session.add(permiso_user_destroy)
    db.session.commit()

permiso_user_update = db.session.query(Permiso).filter_by(
    name='user_update'
    ).first()
if not permiso_user_update:
    permiso_user_update = Permiso(name='user_update')
    db.session.add(permiso_user_update)
    db.session.commit()

permiso_user_show = db.session.query(Permiso).filter_by(
    name='user_show'
    ).first()
if not permiso_user_show:
    permiso_user_show = Permiso(name='user_show')
    db.session.add(permiso_user_show)
    db.session.commit() 

#Creacion tipo de centros de ayuda    
tipo1 = db.session.query(Tipo).filter_by(
    name='Merendero'
    ).first()
if not tipo1:
    tipo1 = Tipo(name='Merendero')
    db.session.add(tipo1)
    db.session.commit()

tipo2 = db.session.query(Tipo).filter_by(
    name='Institución religiosa'
    ).first()
if not tipo2:
    tipo2 = Tipo(name='Institución religiosa')
    db.session.add(tipo2)
    db.session.commit() 

#Creacion de centros de ayuda
centro_aceptado = db.session.query(Centro).filter_by(
    name='Centro 1'
    ).first()
if not centro_aceptado:
    centro_aceptado = Centro(name='Centro 1', 
                     location='Ituzaingo 1079', 
                     phone_number='4032-3243', 
                     start_time='06:30', 
                     final_time='17:00', 
                     municipality='Quilmes', 
                     coordinates='-34.72418 -58.25265', 
                     estado='aceptado')
    db.session.add(centro_aceptado)
    db.session.commit()

centro_pendiente = db.session.query(Centro).filter_by(
    name='Centro 2'
    ).first()
if not centro_pendiente:
    centro_pendiente = Centro(name='Centro 2', 
                     location='Calle 47', 
                     phone_number='221-874-3321', 
                     start_time='08:00', 
                     final_time='16:00', 
                     municipality='La plata', 
                     coordinates='-34.92145 -57.95453')
    db.session.add(centro_pendiente)
    db.session.commit()

centro_rechazado = db.session.query(Centro).filter_by(
    name='Centro 3'
    ).first()
if not centro_rechazado:
    centro_rechazado = Centro(name='Centro 3', 
                     location='Dr Melo 3897', 
                     phone_number='5432-5643', 
                     start_time='09:00', 
                     final_time='16:00', 
                     municipality='Lanús', 
                     coordinates='-34.69941 -58.39263', 
                     estado='rechazado')
    db.session.add(centro_rechazado)
    db.session.commit()    

#Vincular tipo de centro con el centro de ayuda
tipo1.centros.append(centro_aceptado)
tipo1.centros.append(centro_rechazado)
tipo2.centros.append(centro_pendiente)

#Relacionar permisos con rol
rol_admin.permisos.append(permiso_config_index)
rol_admin.permisos.append(permiso_config_new)
rol_admin.permisos.append(permiso_config_destroy)
rol_admin.permisos.append(permiso_config_update)
rol_admin.permisos.append(permiso_config_show)
rol_admin.permisos.append(permiso_user_index)
rol_admin.permisos.append(permiso_user_new)
rol_admin.permisos.append(permiso_user_destroy)
rol_admin.permisos.append(permiso_user_update)
rol_admin.permisos.append(permiso_user_show)

#Relacionar users con el roles
user.roles.append(rol_admin)
user.roles.append(rol_user)
user_operator.roles.append(rol_user)
user_operator.roles.append(rol_operador)
db.session.add(user)
db.session.add(user_operator)
db.session.commit()
