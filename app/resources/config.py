""" 
Manejador de la configuracion
"""
from flask import render_template, session, redirect, url_for, flash
from app.helpers.forms import ConfigForm
from app import db
from app.models.site import Site
from flask_login import login_required
from app.validators.user_validators import check_permission


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
