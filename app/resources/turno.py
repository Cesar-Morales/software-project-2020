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
from datetime import time, date, datetime ,timedelta


@login_required
def index(id=1, page=1):
    """Funcion que muestra el listado de turnos para un determinado centro """
    per_page = Site.page()
    total = Turno.getTurnosByDate(id).count()
    turnos = Turno.getTurnosByDate(id).paginate(page, per_page, False)
    total_pages=int(math.ceil(total/per_page))
    return render_template('turno/index.html', 
                            turnos=turnos, 
                            total_pages=total_pages, 
                            id=id)


@login_required
def new(id=1):
    """Funcion que muestra el listado de turnos para un determinado centro """
    form = TurnoForm()
    form.centro_id.data = id
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
        return redirect(url_for('turno_index', id=form.centro_id.data, page=1))
    return render_template('turno/new.html', form=form)


@login_required
def edit(centro_id, id):
    form = TurnoForm()
    turno = Turno.buscarTurnoPorId(id)
    form.centro_id.data = turno.centro_id
    form.hora_inicio.data = time.fromisoformat(turno.start_time)
    form.fecha.data = date.fromisoformat(turno.date)
    return render_template('turno/edit.html', form=form, id=id)


@login_required
def update(id):

    form = TurnoForm()

    if form.validate():
        if Turno.update(form, id):
            flash('Turno modificado correctamente')
        else:
            flash('El horario ya se encuentra ocupado para la fecha')
        return redirect(url_for('turno_index', 
                        id=form.centro_id.data, 
                        page=1))
    return render_template('turno/edit.html', form=form, id=id)


@login_required
def trash(centro_id,id):
    """Controlador que realiza el intento de borrado de usuario. 
    Se verifica que se este autenticado y que se tengan los permisos. 
    Si alguna verificacion no pasa, se redirecciona segun corresponda. 
    Si pasa las verificaciones, informa estado de operacion segun 
    corresponda"""
    Turno.trash(id)
    return redirect(url_for('turno_index', id=centro_id, page=1))
