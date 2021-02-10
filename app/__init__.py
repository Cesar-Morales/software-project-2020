""" 
Configuración de la aplicación
"""

from os import path, environ
from flask import Flask
from flask_session import Session
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.helpers.format_data import datetimeformat

# Configuración inicial de la app
app = Flask(__name__)

#Secret key para que ande el log-in
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Path de descarga
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Carga de la configuración
env = environ.get("FLASK_ENV")
app.config.from_object(config[env])
#Para que JSON no ordene las keys
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

#Registro del filtro para formatear fechas
app.jinja_env.filters['datetimeformat'] = datetimeformat

# Server Side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configuracion del login
login_manager = LoginManager(app)
login_manager.login_view = "auth_login"
login_manager.login_message = "No esta autorizado para realizar esta operacion"
login_manager.login_message_category = "info"

#Configurar CORS
CORS(app)

#Configurar datos alchemy
#Reducir esta creacion a 79 caracteres por linea
uri = ('mysql://' + app.config["DB_USER"] + ':' + app.config["DB_PASS"] 
       + '@' + app.config["DB_HOST"] + '/' + app.config["DB_NAME"])
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri

#Configure db
db = SQLAlchemy(app)

#Configurar marshmallow
ma = Marshmallow(app)

#Importar creacion inicial de la base de datos
# from app import database_populate

#Importar las rutas de la aplicacion
from app import routes

def create_app():
    return app
