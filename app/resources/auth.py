""" 
Manejador de la sesión
"""

from flask import redirect, render_template
from flask import request, url_for, abort, session, flash
from app.models.user import User
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import login_user, logout_user, login_required
from app.helpers.auth import authenticated


def login():
    return render_template("auth/login.html")


def authenticate():

    if not authenticated(session):
        flash("Acceso prohibido")
        return redirect(url_for("home"))

    params = request.form
    user = db.session.query(User).filter_by(
            email=params["email"], 
            password=params["password"]
            ).first()
    
    if not user:
        flash("Usuario o clave incorrecto.")
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
    session["user"] = user.email
    session["username"] = user.username
    flash("La sesión se inició correctamente.") 

    #Logeo del user
    login_user(user)

    return redirect(url_for("home"))

def logout():
    if not authenticated(session):
        flash("Acceso prohibido")
        return redirect(url_for("home"))
    del session["user"]
    del session["roles"]
    del session["username"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    logout_user()

    return redirect(url_for("auth_login"))
