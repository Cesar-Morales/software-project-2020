""" 
Manejador del user
"""

from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.user import User,Rol
from app.helpers.auth import authenticated
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from app.static.constantes import ITEMS_PERPAGE
import json
from app.helpers.forms import UserForm
from app.validators.user_validators import check_permission



# Protected resources
@login_required
def index():
    if not current_user.is_authenticated:
        abort(401)
    if not check_permission('user_index'):
        flash("No posee los permisos necesarios para poder ver la lista de usuarios")
        return redirect(url_for("home"))
    permiso = check_permission('user_show')
    users = User.getAll()
    return render_template("user/index.html", users=users,sessionIdUser = session["idUserLogged"],tienePermiso=permiso, porPagina=ITEMS_PERPAGE )
    


@login_required
def new():
    if not authenticated(session):
        abort(401)
    if not check_permission('user_new'):
        flash("No posee los permisos necesarios para crear usuarios")
        return redirect(url_for("user_index"))
    form = UserForm()
    return render_template("user/new.html", form=form)     



@login_required
def search():
    if not authenticated(session):
        abort(401)
    if not check_permission('user_index'):
        flash("No posee los permisos necesarios para poder ver la lista de usuarios")
        return redirect(url_for("home"))    
    permiso = check_permission('user_show')
    return render_template("user/index.html", users=User.search(request.form),
                           porPagina=ITEMS_PERPAGE,tienePermiso=permiso,sessionIdUser = session["idUserLogged"])


@login_required
def create():
    if not authenticated(session):
        abort(401)
    if not check_permission('user_new'):
        flash("No posee los permisos necesarios para poder crear usuarios")
        return redirect(url_for("user_index"))    
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
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    if User.block(request.form):
        flash("Bloqueado correctamente")
    else:
        flash("No puedes bloquear a un administrador")
    return index()


@login_required
def activate():
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    if User.activate(request.form):
        flash("Activado correctamente")
    return index()


@login_required
def trash():
    if not check_permission('user_destroy'):
        flash("No posee los permisos necesarios para eliminar usuarios")
        return redirect(url_for("user_index"))
    if User.trash(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'No puedes borrar a un administrador'})    

@login_required
def edit():
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    form = UserForm()
    usuario = User.getUserById(request.form.get('idUser'))
    form.username.data = usuario.username
    form.last_name.data= usuario.last_name
    form.first_name.data = usuario.first_name
    form.email.data = usuario.email
    form.password.data = usuario.password
    form.idUser.data = usuario.id
    roles = Rol.getRoles()
    rolesUser = usuario.roles
    #userDetails = User.getUserById(request.form.get('idUser'))
    return render_template("user/editar.html",form = form,roles = roles, rolesUser = rolesUser)

def confirmEdit():
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
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


   