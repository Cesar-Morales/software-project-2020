from os import path, environ
from flask import Flask
from flask_session import Session
from config import config


from flask_sqlalchemy import SQLAlchemy

environment = "development"

# Configuración inicial de la app
app = Flask(__name__)

# Carga de la configuración
env = environ.get("FLASK_ENV", environment)
app.config.from_object(config[env])

# Server Side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configurar datos alchemy
#Reducir esta creacion a 79 caracteres por linea
uri = 'mysql://' + app.config["DB_USER"] + ':' + app.config["DB_PASS"] + '@' + app.config["DB_HOST"] + '/' + app.config["DB_NAME"]
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Configure db
db = SQLAlchemy(app)  

#Creacion de la base de datos
from app.models.user import User
from app.models.rol import Rol
from app.models.site import Site
from app.models.permiso import Permiso
db.create_all()

#Creación del objeto sistio si no existe
site = db.session.query(Site).first()
if not site:
    site_new = Site(title='AyudAR', 
        email='ayudar@gmail.ar' , 
        description='Sistema de ayuda social')
    
    db.session.add(site_new)
    db.session.commit()

# ----------------     Creación de datos inciales para la apliación             --------------------- 

#Creacion del admin inicial del sistema si no existe
user = db.session.query(User).filter_by(email='admin').first()
if not user:
    user = User(email='admin', 
        last_name='Marcos', 
        first_name='Carlos', 
        password='123123', 
        username='admin')
    
    db.session.add(user)
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

#Crea rol user si no existe. Este se usa cuando apenas se crea un nuevo user.
rol_user = db.session.query(Rol).filter_by(name='user').first()
if not rol_user:
    rol_user = Rol(name='user')

    db.session.add(rol_user)
    db.session.commit()    

#Crear permisos
#Permisos para modulo config
permiso_config_index = db.session.query(Permiso).filter_by(name='config_index').first()
if not permiso_config_index:
    permiso_config_index = Permiso(name='config_index')

    db.session.add(permiso_config_index)
    db.session.commit()

permiso_config_new = db.session.query(Permiso).filter_by(name='config_new').first()
if not permiso_config_new:
    permiso_config_new = Permiso(name='config_new')

    db.session.add(permiso_config_new)
    db.session.commit()

permiso_config_destroy = db.session.query(Permiso).filter_by(name='config_destroy').first()
if not permiso_config_destroy:
    permiso_config_destroy = Permiso(name='config_destroy')

    db.session.add(permiso_config_destroy)
    db.session.commit()

permiso_config_update = db.session.query(Permiso).filter_by(name='config_update').first()
if not permiso_config_update:
    permiso_config_update = Permiso(name='config_update')

    db.session.add(permiso_config_update)
    db.session.commit()

permiso_config_show = db.session.query(Permiso).filter_by(name='config_show').first()
if not permiso_config_show:
    permiso_config_show = Permiso(name='config_show')

    db.session.add(permiso_config_show)
    db.session.commit()

#Permisos para modulo usuario
permiso_user_index = db.session.query(Permiso).filter_by(name='user_index').first()
if not permiso_user_index:
    permiso_user_index = Permiso(name='user_index')

    db.session.add(permiso_user_index)
    db.session.commit()

permiso_user_new = db.session.query(Permiso).filter_by(name='user_new').first()
if not permiso_user_new:
    permiso_user_new = Permiso(name='user_new')

    db.session.add(permiso_user_new)
    db.session.commit()

permiso_user_destroy = db.session.query(Permiso).filter_by(name='user_destroy').first()
if not permiso_user_destroy:
    permiso_user_destroy = Permiso(name='user_destroy')

    db.session.add(permiso_user_destroy)
    db.session.commit()

permiso_user_update = db.session.query(Permiso).filter_by(name='user_update').first()
if not permiso_user_update:
    permiso_user_update = Permiso(name='user_update')

    db.session.add(permiso_user_update)
    db.session.commit()

permiso_user_show = db.session.query(Permiso).filter_by(name='user_show').first()
if not permiso_user_show:
    permiso_user_show = Permiso(name='user_show')

    db.session.add(permiso_user_show)
    db.session.commit()         

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

#Relacionar al admin con el rol de admin
user.roles.append(rol_admin)
user.roles.append(rol_user)
db.session.add(user)
db.session.commit()

#Importar las rutas de la aplicacion
from app import routes