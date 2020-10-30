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
from app.models.site import Site
import math


# Protected resources
@login_required
def index(pages=1):
    """Funcion que muestra el listado de usuarios. Verifica si el usuario esta autenticado, si esta, verifica los permisos, si no tiene, lo devuelve al home, si los tiene
    lo dejo ver el listado. Si no esta autenticado, le mostramos que no tiene autorizacion """
    if not current_user.is_authenticated:
        abort(401)
    if not check_permission('user_index'):
        flash("No posee los permisos necesarios para poder ver la lista de usuarios")
        return redirect(url_for("home"))
    permiso = check_permission('user_show')
    per_page = Site.page()
    total=User.getAll().count()
    users = User.getAll().paginate(pages,per_page,False)
    total_pages=int(math.ceil(total/per_page))
    return render_template("user/index.html", users=users, total_pages=total_pages,tienePermiso=permiso)
    


@login_required
def new():
    """Controlador que renderiza el template para creacion de usuario. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda"""
    if not authenticated(session):
        abort(401)
    if not check_permission('user_new'):
        flash("No posee los permisos necesarios para crear usuarios")
        return redirect(url_for("user_index"))
    form = UserForm()
    return render_template("user/new.html", form=form)     



@login_required
def search():
    """Controlador que lista usuarios segun criterios de busca. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda"""
    if not authenticated(session):
        abort(401)
    if not check_permission('user_index'):
        flash("No posee los permisos necesarios para poder ver la lista de usuarios")
        return redirect(url_for("home"))    
    permiso = check_permission('user_show')
    per_page = Site.page()
    search = request.form.get("search")
    active = request.form.get("active")
    pagesNumber=request.form.get("pageNumber")
    users=User.search(request.form).paginate(pagesNumber,per_page,False)
    total=User.search(request.form).count()
    total_pages=int(math.ceil(total/per_page))
    return render_template("user/index.html", active=active, search=search ,
                             pageNumber=pagesNumber, total_pages=total_pages,
                             users=users,tienePermiso=permiso)


@login_required
def create():
    """Controlador que realiza el intento de creacion de usuario Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda"""
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
    """Controlador que realiza el intento de bloqueo de usuario. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda"""
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    if User.block(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'No puedes bloquear a un administrador'})



@login_required
def activate():
    """Controlador que realiza el intento de activacion de usuario. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda"""
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    if User.activate(request.form):
        return json.dumps({'status':'OK'})


@login_required
def trash():
    """Controlador que realiza el intento de borrado de usuario. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda"""
    if not check_permission('user_destroy'):
        flash("No posee los permisos necesarios para eliminar usuarios")
        return redirect(url_for("user_index"))
    if User.trash(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'No puedes borrar a un administrador'})    

@login_required
def edit():
    """Controlador que se encarga de renderizar el template correspondiente a la edicion del usuario seleccionado. Se obtienen a partir del model, los datos en cuestion
    se muestra el formulario, y las opciones para editar los mismos. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda """
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
    form.image_name= usuario.image_name
    roles = Rol.getRoles()
    rolesUser = usuario.roles
    return render_template("user/editar.html",form = form,roles = roles, rolesUser = rolesUser)

def confirmEdit():
    """Controlador que recibe los datos del template de editar usuario e intenta hacer el update correspondiente. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda"""
    if not check_permission('user_update'):
        flash("No posee los permisos necesarios para modificar usuarios")
        return redirect(url_for("user_index"))
    resu = User.updateUser(request.form,request.files['image']) 
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
    form.image_name= usuario.image_name
    roles = Rol.getRoles()
    rolesUser = usuario.roles
    return render_template("user/editar.html",form = form,roles = roles, rolesUser = rolesUser)

  