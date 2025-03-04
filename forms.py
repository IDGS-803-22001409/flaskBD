from wtforms import Form
from flask_wtf import FlaskForm
 
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa nombre válido')
    ])
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    email = EmailField('email', [validators.Email(message='Ingrese un correo válido')])
    edad = IntegerField('edad')

class UserForm2(Form):
    id = IntegerField('id', [
        validators.NumberRange(min=1, max=20, message='Valor no válido')
    ])
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=4, max=20, message='Requiere min=4 max=20')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El apellido es requerido')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])

 