from app import app
from flask import render_template, send_from_directory
from app.resources import user
from app.resources import auth
from app.resources import config
from app.resources import turno
from app.resources.api import turno as api_turno
from app.helpers import auth as helper_auth
from flask_wtf import FlaskForm
from app.models.site import Site
from app.helpers.forms import SearchForm
# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

# Autenticación
app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

# Rutas de Usuarios
app.add_url_rule("/usuarios", "user_index", user.index)
app.add_url_rule("/usuarios/<int:pages>","user_index", user.index, methods=['GET'])
app.add_url_rule("/usuarios/block", "user_block", user.block,methods=["POST"])
app.add_url_rule("/usuarios/trash", "user_trash", user.trash,methods=["POST"])
app.add_url_rule("/usuarios/editar", "user_edit", user.edit,methods=["POST"])
app.add_url_rule("/usuarios/active", "user_activ", user.activate,methods=["POST"])
app.add_url_rule("/usuarios/edicion", "user_confirmEdit", user.confirmEdit,methods=["POST"])
app.add_url_rule("/usuarios/busqueda", "user_search", user.search,methods=["POST"])
#app.add_url_rule("/usuarios/busqueda/?search=&active=1&submit=Buscar/<int:pages>", "user_search", user.search,methods=["GET"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

# Rutas de Configuracion
app.add_url_rule("/config", "config_index", config.index)
app.add_url_rule("/config", "config_edit", config.edit, methods=["POST"])

#Rutas de turnos
app.add_url_rule("/centros/<int:id>/turnos/<int:page>", "turno_index", turno.index)
app.add_url_rule("/centros/<int:id>/turnos/new", "turno_new", turno.new)
app.add_url_rule("/centros/<int:centro_id>/turnos/<int:id>/edit", "turno_edit", turno.edit)
app.add_url_rule("/turno/create", "turno_create", turno.create, methods=["POST"])
app.add_url_rule("/turno/update/<int:id>", "turno_update", turno.update, methods=["POST"])
app.add_url_rule("/centros/<int:centro_id>/turno/trash/<int:id>", "turno_trash", turno.trash, methods=["POST"])

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    form = SearchForm()
    site = Site.obtain_site()
    return render_template("home.html", form=form, site=site)

# Rutas de API-rest
app.add_url_rule("/centros/<id>/turnos_disponibles", "api_turno_index", api_turno.index, methods=["GET"])
app.add_url_rule("/centros/<id>/reserva", "api_turno_reserva", api_turno.reserva, methods=["POST"])

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