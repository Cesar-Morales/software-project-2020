from flask import render_template, session, request, redirect, url_for, abort, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.widgets.html5 import NumberInput
from app import db
from app.models.site import Site
from app.helpers.auth import authenticated
from flask_login import current_user, login_required

class ConfigForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired('Debe insertar un Titulo')])
    description = StringField('Descripcion', validators=[DataRequired('Debe Insertar Una Descripcion')])
    email = EmailField('Email', validators=[DataRequired('Debe InsertarUn email')])
    pages = IntegerField('Cantidad De Elementos por Pagina', validators=[NumberRange(min=1, max=100, message="Como minimo se debe mostrar 1 elemento por pagina")], widget=NumberInput(min=1, max=100, step=1))
    active = RadioField('Estado Del Sistema', coerce=int, choices=[(1, 'Habilitar'), (0, 'Deshabilitar')])
    submit = SubmitField('Editar')

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