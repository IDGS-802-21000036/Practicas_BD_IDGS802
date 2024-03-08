from flask import Flask, request, render_template, Response, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask import flash
from datetime import datetime, timedelta
from models import db
from models import Alumnos, Venta
from config import DevelopmentConfig
import forms
from sqlalchemy.sql import func, extract
from flask import g
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(error):
    return "{}".format(error), 404

@app.route("/index", methods=['GET', 'POST'])
def index():
    alumn_form = forms.UsersForm2(request.form)
    
    if request.method == "POST" and alumn_form.validate():
        alumno = Alumnos(nombre = alumn_form.nombre.data, 
                      apaterno = alumn_form.apaterno.data, 
                      email = alumn_form.email.data)
        #insert into alumnos values()
        db.session.add(alumno)
        db.session.commit()
    return render_template("index.html", form = alumn_form)

@app.route('/pizzeria', methods=['GET', 'POST'])
def pizzeria():
    venta_form = forms.VentaForm(request.form)
    pizza_form = forms.PizzaForm(request.form)
    busqueda_form = forms.BusquedaForm(request.form)
    if request.method == "POST":
        print("entro al post")
        option = request.form.get('busqueda')
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        print(option)
        ventas = buscar_ventas(option, dia, mes)
        print(ventas)
    else:
        ventas = buscar_ventas("dia", datetime.now().weekday(), datetime.now().month)
        print(ventas)
    total = 0
    for venta in ventas:
        total += venta.total
    return render_template("ABC_Pizzeria.html", form = venta_form, pizza_form = pizza_form, busqueda_form = busqueda_form, ventas = ventas, total = total)



@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    alumno_form = forms.UsersForm2(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno_form.id.data = request.args.get('id')
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apaterno.data = alumno.apaterno
        alumno_form.email.data = alumno.email
        return render_template("eliminar.html", form = alumno_form)
    if request.method == "POST":
        id = request.args.get('id')
        alumno=Alumnos.get(id)
        db.session.delete(alumno)
        db.session.commit()
        #alumno = Alumnos.query.filter_by(id = alumno_form.id.data).delete()
        return redirect(url_for('ABC_Completo'))

@app.route('/ABC_Completo', methods=['GET', 'POST'])
def ABCompleto():
    alumn_form = forms.UsersForm2(request.form)
    alumnos = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", form = alumn_form, alumnos = alumnos)


@app.route("/maestro", methods=['GET', 'POST'])
def maestro():
    maestro_form = forms.TeachersForm(request.form)
    
    if request.method == "POST" and maestro_form.validate():
        maestro = Maestros(nombres = maestro_form.nombres.data, amaterno = maestro_form.amaterno.data, edad = maestro_form.edad.data, anio_ingreso = maestro_form.anio_ingreso.data, sueldo = maestro_form.sueldo.data)
        #insert into alumnos values()
        db.session.add(maestro)
        db.session.commit()
    return render_template("maestro.html", form = maestro_form)

@app.route('/dispatch', methods=['POST'])
def dispatch():
    venta_form = forms.VentaForm(request.form)
    print("validando...")
    print(request.method)
    if request.method == "POST" and venta_form.validate():
        venta = Venta(nombre = venta_form.nombre.data, direccion = venta_form.direccion.data, telefono = venta_form.telefono.data, total = venta_form.total.data, fecha_venta = venta_form.fecha_venta.data)
        db.session.add(venta)
        db.session.commit()
        flash("Se ha realizado la venta")
    return redirect(url_for('pizzeria'))

@app.route('/ABC_Maestro', methods=['GET', 'POST'])
def ABMaestro():
    maestro_form = forms.TeachersForm(request.form)
    maestros = Maestros.query.all()
    
    return render_template("ABC_Maestro.html", form = maestro_form, maestros = maestros)

def buscar_ventas(option, dia, mes):
    if option == "dia":
        ventas = Venta.query.filter(func.DAYOFWEEK(Venta.fecha_venta) == dia).all()
    elif option == "mes":
        ventas = Venta.query.filter(extract('month', Venta.fecha_venta) == mes).all()
    return ventas


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()