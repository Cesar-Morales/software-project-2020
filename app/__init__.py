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
uri = ('mysql://' + app.config["DB_USER"] + ':' + app.config["DB_PASS"] 
       + '@' + app.config["DB_HOST"] + '/' + app.config["DB_NAME"])
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Configure db
db = SQLAlchemy(app)  

#Importar creacion inicial de la base de datos
from app import database_populate

#Importar las rutas de la aplicacion
from app import routes