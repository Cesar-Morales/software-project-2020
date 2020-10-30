from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, IntegerField, SearchField
from wtforms.widgets.html5 import NumberInput
from wtforms.validators import ValidationError
from wtforms_components import DateField, TimeField, DateRange
from datetime import time, date, timedelta

class Form(FlaskForm):
    startdate_field = DateField('Start Date', format='%Y-%m-%d')
    enddate_field = DateField('End Date', format='%Y-%m-%d')
    submit_field = SubmitField('Next')

    def validate_enddate_field(form, field):
        if field.data < form.startdate_field.data:
            raise ValidationError("End date must not be earlier than start date.")

class ConfigForm(FlaskForm):
    """Clase que se encarga de generar formulario para edicion y configuracion del 
    sitio para luego realizar validaciones correspondientes, tanto del lado
    del servidor como del cliente."""
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
                        min=1, max=100,
                        message="Como minimo se debe mostrar 1 elemento por pagina y como maximo 100 por pagina")],
            widget=NumberInput(min=1, max=100, step=1))
    active = RadioField(
             'Estado Del Sistema', coerce=int,
             choices=[(1, 'Habilitar'), (0, 'Deshabilitar')])
    submit = SubmitField('Editar')


class SearchForm(FlaskForm):
    """Clase que se encarga de generar formulario para busqueda de usuarios para luego 
    realizar validaciones correspondientes, tanto del lado
    del servidor como del cliente."""
    search = SearchField(
             'search',
             render_kw={"placeholder": "Ingrese nombre de usuario a buscar"})
    active = RadioField('active', coerce=int,
                        choices=[(1, 'Activos'), (0, 'Bloqueados')], default=1)
    submit = SubmitField('Buscar')

class UserForm(FlaskForm):
    """Clase que se encarga de generar formulario para edicion y creacion de usuarios 
    para luego realizar validaciones correspondientes, tanto del lado
    del servidor como del cliente."""
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
    idUser = HiddenField('idUser')    
    image_name = StringField('NombreImagen')

class TurnoForm(FlaskForm):
    """Clase que se encarga de generar formulario para edicion y creacion de 
    turnos para luego realizar validaciones correspondientes, tanto del lado
    del servidor como del cliente."""
    
    center_id = HiddenField(
            'idUser' ,
            validators=[DataRequired('El id no esta presente')])

    start_time = TimeField(
            'Hora de inicio',
            validators=[DateRange(message='Horario debe estar entre 09:00 y 15:30', 
                                  min=time.fromisoformat('09:00:00'),
                                  max=time.fromisoformat('15:30:00')), 
                        DataRequired('Falta horario de comienzo')])
    date = DateField(
            'Fecha', 
            validators=[DateRange(message='Indique fecha de hoy o posterior', 
                                  min=date.today()), 
                        DataRequired('Falta fecha')])
    submit = SubmitField('Confirmar')

    def validate_start_time(form, field):
        time = field.data
        time_delta =  timedelta(minutes=time.minute)
        multiplo = timedelta(minutes=30)
        #Si no es multiplo de 30 minutos, tirar error.
        if timedelta() != (time_delta % multiplo):
            raise ValidationError("El horario no es multiplo de 30")
 