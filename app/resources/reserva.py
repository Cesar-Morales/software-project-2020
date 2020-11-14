from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.turno import Turno
from app.models.centro import Centro
from app.models.reseva import Reserva
from app.helpers.auth import authenticated
from app import db
from flask_login import current_user, login_required
from app.static.constantes import ITEMS_PERPAGE
from app.validators.user_validators import check_permission
from app.models.site import Site
from app.helpers.forms import ReservaSearch
import math


@login_required
def index(page=1):
    form = ReservaSearch(request.args)
    per_page = Site.page()
    centro_name = form.centro_name.data
    user_email = form.user_email.data
    reservas = Reserva.search(centro_name, 
                              user_email).paginate(page, per_page, False)
    reservas_total = Reserva.search(centro_name, user_email).count()
    total_pages=int(math.ceil(reservas_total/per_page))
    
    return render_template("reserva/index.html",
                           reservas=reservas,
                           page=page,
                           total_pages=total_pages,
                           form_centro=form.centro_name.data,
                           form_user=form.user_email.data)

@login_required
def search(page=1):
    per_page = Site.page()
    form_centro = request.args.get('centro_name')
    form_user = request.args.get('user_email')
    centro_name = form_centro
    user_email = form_user
    reservas = Reserva.search(form_centro, 
                              form_user).paginate(page, per_page, False)
    reservas_total = Reserva.search(centro_name, user_email).count()
    total_pages=int(math.ceil(reservas_total/per_page))
    
    return render_template("reserva/index.html",
                           reservas=reservas,
                           total_pages=total_pages,
                           page=page,
                           form_centro=form_centro,
                           form_user=form_user)
