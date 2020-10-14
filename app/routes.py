from app import app
from flask import render_template
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources import config
from app.resources.api import issue as api_issue
from app.helpers import handler
from app.helpers import auth as helper_auth
from flask_wtf import FlaskForm
from app.static.forms import SearchForm
# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

# Autenticación
app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

# Rutas de Consultas
app.add_url_rule("/consultas", "issue_index", issue.index)
app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

# Rutas de Usuarios
app.add_url_rule("/usuarios", "user_index", user.index)
app.add_url_rule("/usuarios", "user_block", user.block,methods=["POST"])
app.add_url_rule("/usuarios", "user_activ", user.activate,methods=["POST"])
app.add_url_rule("/usuarios/busqueda", "user_search", user.search,methods=["POST"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

# Rutas de Configuracion
app.add_url_rule("/config", "config_index", config.index)
app.add_url_rule("/config", "config_edit", config.edit, methods=["POST"])

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    form = SearchForm()
    return render_template("home.html", form=form)
    
#Las respuestas no van a ser cacheadas
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

# Rutas de API-rest
app.add_url_rule("/api/consultas", "api_issue_index", api_issue.index)

# Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)
# Implementar lo mismo para el error 500 y 401
