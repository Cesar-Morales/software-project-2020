from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.user import User,Rol
from app.models.centro import Centro
from app.helpers.auth import authenticated
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from app.static.constantes import ITEMS_PERPAGE
import json
from app.helpers.forms import CenterNewForm,centerSearchForm
from app.validators.user_validators import check_permission
from app.models.site import Site
import math
@login_required
def new_center():

    if not authenticated(session):
        abort(401)
    # if not check_permission('user_new'):
    #     flash("No posee los permisos necesarios para crear usuarios")
    #     return redirect(url_for("user_index"))
    form = CenterNewForm()
    return render_template("centros/new.html", form = form)

@login_required
def create():  
    form = CenterNewForm()
    if form.validate():
        if Centro.create(form):
            flash("Centro creado correctamente")
        else:
            flash("Ocurrio un error, intente nuevamente.")
        return redirect(url_for("config_center_index"))
    return render_template("config/centers.html", form=form)

def search():
    form = centerSearchForm()
    per_page = Site.page()
    centro_name = form.centro_name.data
    user_email = form.user_email.data
    reservas = Reserva.search(centro_name, 
                              user_email).paginate(page, per_page, False)
    reservas_total = Reserva.search(centro_name, user_email).count()
    total_pages=int(math.ceil(reservas_total/per_page))
    
    return render_template("reserva/index.html",  
                           reservas=reservas, 
                           total_pages=total_pages)
    centros = Centro.search(request.form.get('nombre'))
    return render_template("home.html", centros=centros)