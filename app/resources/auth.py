from flask import redirect, render_template, request, url_for, abort, session, flash
from app.models.user import User
from sqlalchemy.orm import sessionmaker
from app import db


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = db.session.query(User).filter_by(email=params["email"], password=params["password"]).first()
    
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    #Inicio dde variables globales para manejar la sesion actual del user
    #Los roles del user que se logeo
    #Creo el diccionario de roles
    session["roles"] = {
        "admin": False,
        "operador": False,
    }
    for rol in user.roles:
        nombre = rol.name
        session["roles"][nombre] = True

    #El mail del user que se logeo para verificar que para entrar a una pagina hay que estar logeadx    
    session["user"] = user.email
    flash("La sesión se inició correctamente.")  

    return redirect(url_for("home"))


def logout():
    del session["user"]
    del session["roles"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
