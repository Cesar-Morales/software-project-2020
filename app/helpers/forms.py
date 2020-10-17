from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, IntegerField, SearchField
from wtforms.widgets.html5 import NumberInput


class ConfigForm(FlaskForm):
    title = StringField(
            'Titulo',
            validators=[DataRequired('Debe insertar un Titulo')])
    description = StringField(
                  'Descripcion',
                  validators=[DataRequired('Debe Insertar Una Descripcion')])
    email = EmailField(
            'Email',
            validators=[DataRequired('Debe InsertarUn email')])
    pages = IntegerField(
            'Elementos por Pagina',
            validators=[NumberRange(
                        min=1,
                        message="Como minimo se debe mostrar 1 elemento por pagina")],
            widget=NumberInput(min=1, max=100, step=1))
    active = RadioField(
             'Estado Del Sistema', coerce=int,
             choices=[(1, 'Habilitar'), (0, 'Deshabilitar')])
    submit = SubmitField('Editar')


class SearchForm(FlaskForm):
    search = SearchField(
             'search',
             render_kw={"placeholder": "Ingrese nombre de usuario a buscar"})
    active = RadioField('active', coerce=int,
                        choices=[(1, 'Activos'), (0, 'Bloqueados')], default=1)
    submit = SubmitField('Buscar')

class UserForm(FlaskForm):
        email = EmailField(
            'Email',
            validators=[DataRequired('Debe Insertar un email')])
        first_name = StringField(
            'Nombre',
            validators=[DataRequired('Debe insertar un nombre')])
        last_name = StringField(
            'Apellido',
            validators=[DataRequired('Debe insertar un apellido')])
        username = StringField(
            'Nombre de Usuario',
            validators=[DataRequired('Debe insertar un nombre de usuario')])
        submit = SubmitField('Enviar')    
        password = StringField(
            'Contraseña',
            validators=[DataRequired('Debe insertar una contraseña')])
                      