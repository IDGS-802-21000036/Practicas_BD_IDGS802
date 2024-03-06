from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, FloatField, BooleanField
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
    
class VentaForm(Form):
    id = IntegerField("id")
    nombre = StringField("nombre", [validators.DataRequired(message='el campo es requerido'), validators.length(min=4,max=10,message='ingresa nombre valido')])
    direccion = StringField("Direccion", [validators.DataRequired(message='el campo es requerido'), validators.length(min=4,max=10,message='ingresa direccion valida')])
    telefono = StringField("Telefono", [validators.DataRequired(message='el campo es requerido'), validators.length(min=4,max=10,message='ingresa telefono valido')])
    total = FloatField("Total", render_kw={'readonly': True})
    
class PizzaForm(Form):
    tamanioPizza = RadioField("Tamaño de Pizza", choices=[('chica','Chica $40'),('mediana','Mediana $80'),('grande','Grande $120')], default='chica')
    telefono = StringField("Telefono")
    jamon = BooleanField("Jamon $10")
    pinia = BooleanField("Piña $10")
    champinones = BooleanField("Champiñones $10")
    numero_pizzas = IntegerField("Numero de Pizzas", default=1)

class BusquedaForm(Form):
    busqueda = RadioField("Busqueda", choices=[('dia','Dia'),('mes','Mes')], default='dia')
    
    

