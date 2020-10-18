""" 
Manejador del user
"""

from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.user import User
from app.helpers.auth import authenticated
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from app.static.constantes import ITEMS_PERPAGE
import json
from app.helpers.forms import UserForm

# Protected resources
@login_required
def index():
    if not current_user.is_authenticated:
        abort(401)
    users = User.getAll()
    return render_template("user/index.html", users=users,sessionIdUser = session["idUserLogged"] )
    


@login_required
def new():
    if not authenticated(session):
        abort(401)
    form = UserForm()
    return render_template("user/new.html", form=form)     



@login_required
def search():
    if not authenticated(session):
        abort(401)
    #CESAR aca te dejo el comentario para que se entienda.... le mando al template los usuarios que requieren en la busqueda
    # y le mando la cantidad de registros por pagina, segun la configuracion del sitio, lo atrapas en el html como la variable:
    # porPagina     
    return render_template("user/index.html", users=User.search(request.form),
                           porPagina=ITEMS_PERPAGE,sessionIdUser = session["idUserLogged"])


@login_required
def create():
    if not authenticated(session):
        abort(401)
    form = UserForm()
    if form.validate():
        if User.create(form, request.files['image']):
            flash("Usuario creado correctamente")
        else:
            flash("Usuario o email en uso.")
        return redirect(url_for("user_index"))
    return render_template("user/new.html", form=form)

  


@login_required
def block():
    if User.block(request.form):
        flash("Bloqueado correctamente")
    else:
        flash("No puedes bloquear a un administrador")
    return index()


@login_required
def activate():
    if User.activate(request.form):
        flash("Activado correctamente")
    return index()


@login_required
def trash():
    if User.trash(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'No puedes borrar a un administrador'})    

@login_required
def edit():
    form = UserForm()
    usuario = User.getUserById(request.form.get('idUser'))
    form.username.data = usuario.username
    form.last_name.data= usuario.last_name
    form.first_name.data = usuario.first_name
    form.email.data = usuario.email
    form.password.data = usuario.password
    form.idUser.data = usuario.id
    #userDetails = User.getUserById(request.form.get('idUser'))
    return render_template("user/editar.html",form = form)

def confirmEdit():
    resu = User.updateUser(request.form) 
    if resu == 1:
        flash("editado correctamente")
    else:
        if resu == 2:
            flash("Debe Completar Todos Los Datos")
        else:
            flash("Usuario o Email en uso")      
    form = UserForm()
    usuario = User.getUserById(request.form.get('idUser'))
    form.username.data = usuario.username
    form.last_name.data= usuario.last_name
    form.first_name.data = usuario.first_name
    form.email.data = usuario.email
    form.password.data = usuario.password 
    form.idUser.data = usuario.id
    return render_template("user/editar.html", form = form)


   