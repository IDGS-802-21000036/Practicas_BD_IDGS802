from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import flash
from models import db
from models import Alumnos, Maestros
from config import DevelopmentConfig
import forms
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

@app.route('/ABC_Maestro', methods=['GET', 'POST'])
def ABMaestro():
    maestro_form = forms.TeachersForm(request.form)
    maestros = Maestros.query.all()
    
    return render_template("ABC_Maestro.html", form = maestro_form, maestros = maestros)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()