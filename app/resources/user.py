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

# Protected resources
@login_required
def index():
   
    users = db.session.query(User).all()

    return render_template("user/index.html", users=users)

@login_required
def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

@login_required
def search():
    return render_template("user/index.html",users=User.search(request.form))

@login_required
def create():
    if not authenticated(session):
        abort(401)

    if User.create(request.form):
        flash("Usuario creado correctamente")
    else:
        flash("Usuario o email en uso.")    

    return redirect(url_for("user_index"))
