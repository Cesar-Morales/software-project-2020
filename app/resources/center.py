from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.user import User,Rol
from app.models.centro import Centro
from app.models.tipo import Tipo
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
from datetime import time

# @login_required
def new_center():
    
    if not check_permission('centro_new'):
         flash("No posee los permisos necesario para poder crear centro")
         return redirect(url_for("home"))
    form = CenterNewForm()
    form.municipalidad.data = ''
    center_types = Tipo.getAllTypes()
    form.tipo.choices = [(tipo.name, tipo.name) for tipo in center_types]
    return render_template("centros/new.html", form = form)

@login_required
def create():  

    if not check_permission('centro_new'):
        flash("No posee los permisos necesario para poder crear centro")
        return redirect(url_for("home"))

    form = CenterNewForm()
    form.instrucciones.data = request.files['file'].filename
    if form.validate():
        if Centro.create(form, request.files['file']):
            flash("Centro creado correctamente")
        else:
            flash("Ocurrio un error, intente nuevamente.")
        return redirect(url_for("config_center_index"))

    center_types = Tipo.getAllTypes()
    form.tipo.choices = [(tipo.name, tipo.name) for tipo in center_types]

    return render_template("centros/new.html", form=form)

@login_required
def search(page=1):

    if not check_permission('centro_index'):
        flash("No posee los permisos necesario para poder listar centros")
        return redirect(url_for("home"))

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

    if not check_permission('centro_destroy'):
        flash("No posee los permisos necesario para poder eliminar centro")
        return json.dumps({'status':'No posee los pormisos para borrar centros'})

    if Centro.trashOrReject(request.form):
        return json.dumps({'status':'OK'})
    else:
        return json.dumps({'status':'Ocurrio algun error'})     

@login_required
def edit():

    if not check_permission('centro_update'):
        flash("No posee los permisos necesario para poder editar centro")
        return redirect(url_for("home"))

    form = CenterNewForm()

    centro = Centro.getCentro(request.form.get('center_edit'))

    form.hora_cierre.data = time.fromisoformat(centro.final_time)
    form.hora_apertura.data = time.fromisoformat(centro.start_time)
    form.telefono.data = centro.phone_number
    form.direccion.data = centro.location
    form.nombre.data = centro.name
    form.municipalidad.data = centro.municipality
    form.web.data = centro.web
    form.email.data = centro.email
    form.instrucciones.data = centro.pdf_name
    form.coordenadas.data = centro.coordinates

    center_types = Tipo.getAllTypes()
    form.tipo.choices = [(tipo.name, tipo.name) for tipo in center_types]

    return render_template("centros/edit.html", form = form, center_edit=request.form.get('center_edit'))

@login_required
def confirmEdit():

    if not check_permission('centro_update'):
        flash("No posee los permisos necesario para poder editar centro")
        return redirect(url_for("home"))

    form = CenterNewForm()
    if form.validate():
        if Centro.updateCentro(form, request.form.get('center_edit'), request.files['file']):
            flash("Centro modificado correctamente")
            centro = Centro.getCentro(request.form.get('center_edit'))
            form.hora_cierre.data = time.fromisoformat(centro.final_time)
            form.hora_apertura.data = time.fromisoformat(centro.start_time)
            form.telefono.data = centro.phone_number
            form.direccion.data = centro.location
            form.nombre.data = centro.name
            form.municipalidad.data = centro.municipality
            form.web.data = centro.web
            form.email.data = centro.email
            form.instrucciones.data = centro.pdf_name
            form.coordenadas.data = centro.coordinates
        else:
            flash("Ocurrio un error, intente nuevamente.")

    centerTypes = Tipo.getAllTypes()
    form.tipo.choices = [(tipo.name, tipo.name) for tipo in centerTypes]

    return render_template("centros/edit.html",form = form,center_edit=request.form.get('center_edit'))

def map():
    return render_template("config/map.html")
