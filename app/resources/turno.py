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

@login_required
def index(id=1,pages=1):
    """Funcion que muestra el listado de turnos para un determinado centro """
    per_page = Site.page()
    total = Centro.getAllTurnos(id).count()
    turnos = Centro.getAllTurnos(id).paginate(pages,per_page,False)
    total_pages=int(math.ceil(total/per_page))
    form = TurnoForm()
    form.center_id = id
    return render_template("turno/index.html", turnos=turnos, total_pages=total_pages, form=form)

@login_required
def create():
    """Funcion que crea un nuevo turno para un determinado centro de ayuda"""
    form = TurnoForm()

    if form.validate:
        
        return True

    return redirect(url_for('turno_index'))