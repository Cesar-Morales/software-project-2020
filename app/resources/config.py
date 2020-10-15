""" 
Manejador de la configuracion
"""
from flask import render_template, session, redirect, url_for, flash
from app.helpers.forms import ConfigForm
from app import db
from app.models.site import Site
from flask_login import login_required


@login_required
def index():
    if not session["roles"]["admin"]:
        flash("No posee los permisos necesario para poder acceder a este modulo")
        return redirect(url_for("home"))

    site = db.session.query(Site).first()
    form = ConfigForm()
    form.title.data = site.title
    form.description.data = site.description
    form.email.data = site.email
    form.pages.data = site.pages
    form.active.data = site.active
    return render_template("config/index.html", form=form)


@login_required
def edit():
    site = db.session.query(Site).first()
    form = ConfigForm()
    if form.validate():
        title = form.title.data
        description = form.description.data
        email = form.email.data
        pages = form.pages.data
        active = form.active.data
        site.title = title
        site.description = description
        site.email = email
        site.pages = pages
        site.active = active
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("config/index.html", form=form)
