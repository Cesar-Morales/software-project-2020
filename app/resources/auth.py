""" 
Manejador de la sesión
"""

from flask import redirect, render_template
from flask import request, url_for, abort, session, flash
from app.models.user import User
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import login_user, logout_user


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = User.getUserByEmailAndPassword(params["email"],params["password"])
    #Agregado condicion para que si el usuario que intenta acceder esta bloqueado, no pueda.
    if user.active == 0 :
        flash("Usted esta bloqueado. Contactese con un administrador")
        return redirect(url_for("auth_login"))
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
    del session["user"]
    del session["roles"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    logout_user()

    return redirect(url_for("auth_login"))
