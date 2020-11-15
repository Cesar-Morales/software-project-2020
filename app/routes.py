from app import app
from flask import render_template, send_from_directory
from app.resources import user
from app.resources import center
from app.resources import auth
from app.resources import config
from app.resources import turno
from app.resources import reserva
from app.resources.api import turno as api_turno
from app.resources.api import centro as api_centro
from app.helpers import auth as helper_auth
from flask_wtf import FlaskForm
from app.models.site import Site
from app.models.reseva import Reserva
from app.helpers.forms import SearchForm, ReservaSearch, CenterSearchForm

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

# Autenticación
app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

# Rutas de Usuarios
app.add_url_rule("/usuarios", "user_index", user.index)
app.add_url_rule("/usuarios/<int:page>","user_index", user.index, methods=['GET'])
app.add_url_rule("/usuarios/block", "user_block", user.block,methods=["POST"])
app.add_url_rule("/usuarios/trash", "user_trash", user.trash,methods=["POST"])
app.add_url_rule("/usuarios/editar", "user_edit", user.edit,methods=["POST"])
app.add_url_rule("/usuarios/active", "user_activ", user.activate,methods=["POST"])
app.add_url_rule("/usuarios/edicion", "user_confirmEdit", user.confirmEdit,methods=["POST"])
app.add_url_rule("/usuarios/busqueda", "user_search", user.search,methods=["GET"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

# Rutas de Configuracion
app.add_url_rule("/config", "config_index", config.index)
app.add_url_rule("/config", "config_edit", config.edit, methods=["POST"])

# Rutas de Centros
app.add_url_rule("/config/centers","config_center_index",config.center_index)
app.add_url_rule("/centros/nuevo","centros_new",center.new_center)
app.add_url_rule("/centros/create", "center_create", center.create, methods=["POST"])
app.add_url_rule("/centros/busqueda", "center_search", center.search,methods=["POST"])
app.add_url_rule("/centros/<int:page>", "center_search", center.search, methods=["GET"])
app.add_url_rule("/centros/accept", "center_accept", center.accept, methods=["POST"])
app.add_url_rule("/centros/trashOrReject", "center_trashOrReject", center.trashOrReject, methods=["POST"])
app.add_url_rule("/centros/edit", "center_edit", center.edit, methods=["POST"])

app.add_url_rule("/centros/map","center_map",center.map)

#Rutas de turnos
app.add_url_rule("/centros/<int:id>/turnos/<int:page>", "turno_index", turno.index)
app.add_url_rule("/centros/<int:id>/turnos/new", "turno_new", turno.new)
app.add_url_rule("/centros/<int:centro_id>/turnos/<int:id>/edit", "turno_edit", turno.edit)
app.add_url_rule("/turno/create", "turno_create", turno.create, methods=["POST"])
app.add_url_rule("/turno/update/<int:id>", "turno_update", turno.update, methods=["POST"])
app.add_url_rule("/centros/<int:centro_id>/turno/trash/<int:id>", "turno_trash", turno.trash, methods=["POST"])

# Rutas de reserva
app.add_url_rule("/reservas/<int:page>", "reserva_search", reserva.search, methods=["GET"])

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    form = SearchForm()
    form.page.data = 1
    form_reserva = ReservaSearch()
    reservas = Reserva.getAll()
    emails = []
    for reserva in reservas:
        emails.append(reserva.email)
    emails = list(dict.fromkeys(emails))
    form_reserva.user_email.choices = [("", "---")] + [(email, email) for email in emails]
    formCenterSearch = CenterSearchForm()
    formCenterSearch.options.choices = ["","aceptado","rechazado","pendiente"]
    site = Site.obtain_site()
    return render_template("home.html", 
                            form=form, 
                            form_reserva=form_reserva, 
                            site=site, 
                            centerForm = formCenterSearch)

# Rutas de API-rest
#Turnos
app.add_url_rule("/centros/<id>/turnos_disponibles", "api_turno_index", api_turno.index, methods=["GET"])
app.add_url_rule("/centros/<id>/reserva", "api_turno_reserva", api_turno.reserva, methods=["POST"])

#Centros
app.add_url_rule("/centros", "api_centro_index", api_centro.index, methods=["GET"])
app.add_url_rule("/centros/<centro_id>", "api_centro_show", api_centro.show, methods=["GET"])
app.add_url_rule("/centros", "api_centro_create", api_centro.create, methods=["POST"])

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
