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
def search(page=1):
    per_page = Site.page()
    centro_name = request.args.get('centro_name')
    user_email = request.args.get('user_email')
    reservas = Reserva.search(centro_name, 
                              user_email).paginate(page, per_page, False)
    reservas_total = Reserva.search(centro_name, user_email).count()
    total_pages=int(math.ceil(reservas_total/per_page))
    
    return render_template("reserva/index.html",
                           reservas=reservas,
                           total_pages=total_pages,
                           page=page,
                           form_centro=centro_name,
                           form_user=user_email)
