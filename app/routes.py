from app import app
from flask import render_template, send_from_directory
from app.resources import user
from app.resources import center
from app.resources import auth
from app.resources import config
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

# Rutas de Centros
app.add_url_rule("/config/centers","config_center_index",config.center_index)
app.add_url_rule("/centros/nuevo","centros_new",center.new_center)

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    form = SearchForm()
    site = Site.obtain_site()
    return render_template("home.html", form=form, site=site)

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