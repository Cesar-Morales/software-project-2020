from app import app
from flask import render_template, send_from_directory
from app.resources import user
from app.resources import auth
from app.resources import config
from app.helpers import auth as helper_auth

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

# Autenticación
app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

# Rutas de Usuarios
app.add_url_rule("/usuarios", "user_index", user.index)
app.add_url_rule("/usuarios/busqueda", "user_search", user.search,methods=["POST"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

# Rutas de Configuracion
app.add_url_rule("/config", "config_index", config.index)
app.add_url_rule("/config", "config_edit", config.edit, methods=["POST"])

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    return render_template("home.html")

#Rutas estaticas de las imagenes
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

#Las respuestas no van a ser cacheadas
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response