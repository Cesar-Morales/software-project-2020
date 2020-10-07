from flask import render_template, session, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField
from app import db
from app.models.site import Site

class ConfigForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired('Debe insertar un Titulo')])
    description = StringField('Descripcion', validators=[DataRequired('Debe Insertar Una Descripcion')])
    email = EmailField('Email', validators=[DataRequired('Debe InsertarUn email')])
    pages = IntegerField('Cantidad De Elementos por Pagina', validators=[NumberRange(min=1, message="Como minimo se debe mostrar 1 elemento por pagina")])
    active = RadioField('Estado Del Sistema', coerce=bool, choices=[(True, 'Habilitar'), (False, 'Deshabilitar')])
    submit = SubmitField('Editar')

def index():
    site = db.session.query(Site).first()
    form = ConfigForm()
    form.title.data = site.title
    form.description.data = site.description
    form.email.data = site.email
    form.pages.data = site.pages
    form.active.data = site.active
    return render_template("config/index.html", form=form)

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