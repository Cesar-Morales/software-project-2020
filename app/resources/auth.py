""" 
Manejador de la sesión
"""

from flask import redirect, render_template
from flask import request, url_for, abort, session, flash
from app.models.user import User
from app.models.site import Site
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import login_user, logout_user, login_required
from app.helpers.auth import authenticated


def login():
    if not authenticated(session):
        return render_template("auth/login.html")
    else:
        return redirect(url_for("home"))


def authenticate():
    """Controlador que se encarga de autenticar al usuario que intenta loguearse. Si pasa la autenticacion, se procede a guardar los datos
    del usuario en la sesion asi como tambien los roles que posee."""
    params = request.form
    user = User.getUserByEmailAndPassword(params["email"],params["password"])
    #Agregado condicion para que si el usuario que intenta acceder esta bloqueado, no pueda.
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    if user.active == 0 :
        flash("Usted esta bloqueado. Contactese con un administrador")
        return redirect(url_for("auth_login"))
    

    #Inicio dde variables globales para manejar la sesion actual para user
    #Los roles para user que se logeo
    #Creo el diccionario de roles
    session["roles"] = {
        "admin": False,
        "operador": False,
        "user" : False
        }

    #Vuelvo verdadera los roles que posee user
    for rol in user.roles:
        nombre = rol.name
        session["roles"][nombre] = True

    #El mail para user que se logeo para verificar que para entrar 
    #a una pagina hay que estar logeadx
    if (Site.obtain_site().active or session["roles"]["admin"]):
        session["user"] = user.email
        session["username"] = user.username
        session["idUserLogged"] = user.id
        flash("La sesión se inició correctamente.")

        #Logeo del user
        login_user(user)

        return redirect(url_for("home"))
    else:
        del session["roles"]
        flash("La pagina se encuentra en mantenimiento. Intente mas tarde")
        return redirect(url_for("auth_login"))

def logout():
    """Controlador que se encarga de cerrar la sesion del usuario actual logueado. Verifica que se este autenticado; si pasa, se procede a eliminar 
    los datos de la session"""
    if not authenticated(session):
        flash("Acceso prohibido")
        return redirect(url_for("home"))
    del session["user"]
    del session["roles"]
    del session["username"]
    del session["idUserLogged"]
    flash("La sesión se cerró correctamente.")

    logout_user()

    return redirect(url_for("auth_login"))
