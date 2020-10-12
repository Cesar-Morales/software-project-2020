from os import path, environ
from flask import Flask
from flask_session import Session
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

environment = "development"

# Configuración inicial de la app
app = Flask(__name__)

#Secret key para que ande el log-in
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Carga de la configuración
env = environ.get("FLASK_ENV", environment)
app.config.from_object(config[env])

# Server Side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configuracion del login
login_manager = LoginManager(app)
login_manager.login_view = "auth_login"
login_manager.login_message = "Este mesaje se muestra cuando volves de una pagina a la que queres acceder sin estar loged. Se puede modificar el estilo cambiando la categoria en __init__"
login_manager.login_message_category = "info"


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

#Relacionar al admin con el rol de admin
user.roles.append(rol_admin)
db.session.add(rol_admin)
db.session.commit()

#Importar las rutas de la aplicacion
from app import routes