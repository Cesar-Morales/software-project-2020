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
# Protected resources
@login_required
def index():
    if not current_user.is_authenticated:
        abort(401)
   
    users = db.session.query(User).all()

    return render_template("user/index.html", users=users)

@login_required
def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

@login_required
def search():
    if not authenticated(session):
        abort(401)
    #CESAR aca te dejo el comentario para que se entienda.... le mando al template los usuarios que requieren en la busqueda
    # y le mando la cantidad de registros por pagina, segun la configuracion del sitio, lo atrapas en el html como la variable:
    # porPagina     
    return render_template("user/index.html",users=User.search(request.form), porPagina=ITEMS_PERPAGE)

@login_required
def create():
    if not authenticated(session):
        abort(401)

    if User.create(request.form):
        flash("Usuario creado correctamente")
    else:
        flash("Usuario o email en uso.")    

    return redirect(url_for("user_index"))

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
        flash("activado correctamente")
    return index()    

@login_required
def trash():
    if User.trash(request.form):
        flash("borrado correctamente")
    else:
        flash("No puedes borrar a un administrador")      
    return index()        