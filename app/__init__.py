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

#Creación del objeto sistema que
site = db.session.query(Site).first()
if not site:
    site_new = Site(title='AyudAR', email='ayudar@gmail.ar' , description='Sistema de ayuda social')
    db.session.add(site_new)
    db.session.commit()    

#Importar las rutas de la aplicacion
from app import routes

