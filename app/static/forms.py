from flask import render_template, session, request, redirect, url_for, abort
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, IntegerField, SearchField
from wtforms.widgets.html5 import NumberInput
from app import db
from app.models.site import Site
from app.helpers.auth import authenticated

class SearchForm(FlaskForm):
    search = SearchField('search', render_kw={"placeholder": "Ingrese nombre de usuario a buscar"})
    active = RadioField('active', coerce=int, choices=[(1, 'Activos'), (0, 'Bloqueados')],default=1)
    submit = SubmitField('Buscar')

