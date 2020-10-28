from flask import redirect, render_template, request
from flask import url_for, session, abort, flash
from app.models.user import User,Rol
from app.helpers.auth import authenticated
from sqlalchemy.orm import sessionmaker
from app import db
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from app.static.constantes import ITEMS_PERPAGE
import json
from app.helpers.forms import CenterNewForm
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