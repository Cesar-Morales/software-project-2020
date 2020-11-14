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
from app.helpers.forms import CenterNewForm, CenterSearchForm
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
    return render_template("centros/new.html", form=form)

@login_required
def search(page=1):
    per_page = Site.page()
    search = request.args.get('search')
    options = request.args.get('options')
    centros = Centro.search(search,options).paginate(page, per_page, False)
    centros_total = Centro.search(search, options).count()
    total_pages=int(math.ceil(centros_total/per_page))
    
    return render_template("centros/index.html",  
                           centros=centros,
                           total_pages=total_pages,
                           page=page,
                           search=search,
                           options=options)

@login_required
def accept():
    if Centro.accept(request.form):
        return json.dumps({'status':'OK'})

@login_required
def trashOrReject():

    if Centro.trashOrReject(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'Ocurrio algun error'})     

def map():
    return render_template("config/map.html")
