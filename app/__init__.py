from os import path, environ
from flask import Flask, render_template, g
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


#Configurar datos alchemy
uri = 'mysql://' + app.config["DB_USER"] + ':' + app.config["DB_PASS"] + '@' + app.config["DB_HOST"] + '/' + app.config["DB_NAME"]
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Configure db
db = SQLAlchemy(app)  

Session(app)
