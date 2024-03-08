from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, FloatField, BooleanField, DateField
from wtforms import validators
from datetime import datetime
    
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
    fecha_venta = DateField("Fecha de Venta", format='%Y-%m-%d', default=datetime.now(), validators=[validators.DataRequired(message='el campo es requerido')])
    total = FloatField("Total", render_kw={'readonly': True})
    
class PizzaForm(Form):
    id = IntegerField("id")
    tamanioPizza = RadioField("Tamaño de Pizza", choices=[('chica','Chica $40'),('mediana','Mediana $80'),('grande','Grande $120')], default='chica')
    jamon = BooleanField("Jamon $10")
    pinia = BooleanField("Piña $10")
    champinones = BooleanField("Champiñones $10")
    numero_pizzas = IntegerField("Numero de Pizzas", default=1, validators=[validators.DataRequired(message='el campo es requerido'), validators.NumberRange(min=1, max=10, message='ingresa un numero valido')])

class BusquedaForm(Form):
    busqueda = RadioField("Busqueda", choices=[('dia','Dia'),('mes','Mes')], default='dia')
    fecha = DateField("Fecha", format='%Y-%m-%d', default=datetime.now(), validators=[validators.DataRequired(message='el campo es requerido')])
    dia = SelectField("Dia", choices=[('2','Lunes'), ('3', 'Martes'),
                                      ('4','Miercoles'), ('5', 'Jueves'),
                                      ('6','Viernes'), ('7', 'Sabado'),
                                      ('1','Domingo')], default='2')
    mes = SelectField("Mes", choices=[('1','Enero'), ('2', 'Febrero'), 
                                      ('3', 'Marzo'), ('4', "Abril"), 
                                      ('5', 'Mayo'), ('6', "Junio"), 
                                      ('7', 'Julio'), ('8', "Agosto"), 
                                      ('9', 'Septiembre'), ('10', "Ocutbre"), 
                                      ('11', 'Noviembre'), ('12', "Diciembre")], default='1')
    
    

