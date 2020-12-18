""" 
Manejador de la configuracion
"""
from flask import render_template, session, redirect, url_for, flash, request
from app.helpers.forms import ConfigForm
from app import db
from app.models.site import Site
from app.models.centro import Centro
from flask_login import login_required
from app.validators.user_validators import check_permission
import math


@login_required
def index():
    """Este metodo renderiza el template correspondiente a la configuracion del sitio. Se verifican los permisos necesarios, y que se este autenticado. Si no cumple 
    con alguno de los dos, se devuelve mensaje correspondiente."""
    
    if not check_permission('config_show'):
        flash("No posee los permisos necesario para poder ver los datos del sitio")
        return redirect(url_for("home"))

    site = Site.obtain_site()
    form = ConfigForm()
    form.title.data = site.title
    form.description.data = site.description
    form.email.data = site.email
    form.pages.data = site.pages
    form.active.data = site.active
    return render_template("config/index.html", form=form)


@login_required
def edit():
    """Este metodo se encarga de intentar actualizar los datos del sitio, segun modificaciones correspondientes a formulario de edicion. Se verifican
    los permisos y autenticacion: si no pasan, se devuelve mensaje correspondiente. """
    
    form = ConfigForm()
    
    if not check_permission('config_update'):
        flash("No posee los permisos necesario para poder editar el sitio")
        return render_template("config/index.html", form=form)    
    
    if form.validate():
        title = form.title.data
        description = form.description.data
        email = form.email.data
        pages = form.pages.data
        active = form.active.data
        Site.update_data(title,description,email,pages,active)
        return redirect(url_for('home'))
    return render_template("config/index.html", form=form)

@login_required
def center_index(modal='pendiente'):

    if not check_permission('centro_index'):
        flash("No posee los permisos necesario para poder listar centros")
        return redirect(url_for("home"))

    #como para empezar me traigo todos los centros cargados, para ver si funciona. 
    
    permiso = check_permission('center_show')

    #Obtener parametros de url
    if(request.args.get('modal')):
        modal = request.args.get('modal')


    page_pendiente = int(request.args.get('page_pendiente'))
    page_aceptado = int(request.args.get('page_aceptado'))
    page_rechazado = int(request.args.get('page_rechazado'))



    per_page = Site.page()

    #Centros pendientes
    total_pendientes = Centro.getAllPendientes().count()
    centers_pendientes = Centro.getAllPendientes().paginate(page_pendiente,per_page,False)
    total_pages_pendientes=int(math.ceil(total_pendientes/per_page))

    #Centros aceptaos
    total_aceptados = Centro.getAllAceptados().count()
    centers_aceptados = Centro.getAllAceptados().paginate(page_aceptado,per_page,False)
    total_pages_aceptadas=int(math.ceil(total_aceptados/per_page))

    #Centros rechazado
    total_rechazados = Centro.getAllRechazados().count()
    centers_rechazados = Centro.getAllRechazados().paginate(page_rechazado,per_page,False)
    total_pages_rechazados=int(math.ceil(total_rechazados/per_page))
    
    return render_template("config/centers.html", 
                           centers_aceptados = centers_aceptados, 
                           total_pages_aceptadas=total_pages_aceptadas, 
                           centers_pendientes = centers_pendientes, 
                           total_pages_pendientes=total_pages_pendientes, 
                           centers_rechazados = centers_rechazados, 
                           total_pages_rechazados=total_pages_rechazados, 
                           tienePermiso=permiso,
                           modal=modal,
                           page_pendiente=page_pendiente,
                           page_aceptado=page_aceptado,
                           page_rechazado=page_rechazado)
