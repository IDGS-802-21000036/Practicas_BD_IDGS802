from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, FloatField
from wtforms import validators
    
class TeachersForm(Form):
    id = IntegerField("id")	
    nombres = StringField("nombre",[validators.DataRequired(message='el campo es requerido'), validators.length(min=4,max=10,message='ingresa nombre valido')])
    amaterno = StringField("apaterno")
    edad = IntegerField("edad")
    anio_ingreso = IntegerField("anio_ingreso")
    sueldo = FloatField("sueldo")
    
class UsersForm2(Form):
    id = IntegerField("id")	
    nombre = StringField("nombre",[validators.DataRequired(message='el campo es requerido'), validators.length(min=4,max=10,message='ingresa nombre valido')])
    apaterno = StringField("apaterno")
    email = EmailField("correo",[validators.Email(message='Ingrese un correo valido')])

