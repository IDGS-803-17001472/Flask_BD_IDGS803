from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    amaterno = StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    edad = IntegerField('edad', [
       validators.number_range(min=1, max=20, message='valor no valido')
    ])
    email = EmailField('email',[
        validators.Email(message='Ingrese un correo válido')
    ])

class DicRegistroForm(Form):
    txtPalaIngles=StringField('txtPalaIngles',[
        validators.DataRequired(message='el campo es requerido')
    ])
    txtPalaEsp=StringField('txtPalaEsp',[
        validators.DataRequired(message='el campo es requerido')
    ])
class DicTraerPalabra(Form):
    txtPalaIngles=StringField('txtPalaIngles',[
        validators.DataRequired(message='el campo es requerido')
    ])
    txtPalaEsp=StringField('txtPalaEsp',[
        validators.DataRequired(message='el campo es requerido')
    ])