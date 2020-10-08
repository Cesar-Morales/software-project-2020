from app import app
from flask import render_template
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources.api import issue as api_issue
from app.helpers import handler
from app.helpers import auth as helper_auth

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
app.add_url_rule("/usuarios/busqueda", "user_search", user.search,methods=["POST"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    return render_template("home.html")

# Rutas de API-rest
app.add_url_rule("/api/consultas", "api_issue_index", api_issue.index)

# Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)
# Implementar lo mismo para el error 500 y 401
