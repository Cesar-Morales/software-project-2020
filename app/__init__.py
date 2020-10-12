""" 
Configuración de la aplicación
"""

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