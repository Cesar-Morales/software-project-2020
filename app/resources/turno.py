from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.turno import Turno
from app.models.centro import Centro
from app.helpers.auth import authenticated
from app import db
from flask_login import current_user, login_required
from app.static.constantes import ITEMS_PERPAGE
from app.validators.user_validators import check_permission
from app.models.site import Site
from app.helpers.forms import TurnoForm
import math
from datetime import time, timedelta


@login_required
def index(id=1, page=1):
    """Funcion que muestra el listado de turnos para un determinado centro """
    per_page = Site.page()
    total = Centro.getAllTurnos(id).count()
    turnos = Centro.getAllTurnos(id).paginate(page, per_page, False)
    total_pages=int(math.ceil(total/per_page))
    return render_template('turno/index.html', turnos=turnos, total_pages=total_pages, id=id)


@login_required
def new(id=1):
    """Funcion que muestra el listado de turnos para un determinado centro """
    form = TurnoForm()
    form.center_id.data = id
    return render_template('turno/new.html', form=form)


@login_required
def create():
    """Funcion que crea un nuevo turno para un determinado centro de ayuda"""
    form = TurnoForm()

    if form.validate():
        if Turno.create(form):
            flash('Turno creado correctamente')
        else:
            flash('El horario ya se encuentra ocupado para la fecha')
        return redirect(url_for('turno_index', id=form.center_id.data, page=1))
    return render_template('turno/new.html', form=form)


@login_required
def edit(centro_id, turno_id):
    form = TurnoForm()
    turno = db.session.query(Turno).filter_by(id=turno_id).first()
    form.center_id.data = turno.centro_id
    form.start_time.data = turno.start_time
    form.date.data = turno.date
    return render_template('turno/edit.html', form=form)


@login_required
def update():
    form = TurnoForm()
    if form.validate():
        if Turno.update(form):
            flash('Turno modificado correctamente')
        else:
            flash('El horario ya se encuentra ocupado para la fecha')
        return redirect(url_for('turno_index', id=form.center_id.data, page=1))
    return render_template('turno/edit.html', form=form)


@login_required
def trash(id):
    """Controlador que realiza el intento de borrado de usuario. Se verifica que se este autenticado y que se tengan los permisos. Si
    alguna verificacion no pasa, se redirecciona segun corresponda. Si pasa las verificaciones, informa estado de operacion segun corresponda"""
    Turno.trash(id)
