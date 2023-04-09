from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojos
from flask_app.models.ninjas import Ninjas

@app.route('/', methods = ['GET' ,'POST'])          
def all_dojos():
    dojos = Dojos.get_all_dojos()
    return render_template("main_page.html", all_dojos = dojos)

@app.route('/create_dojo', methods = ['GET', 'POST'])
def create_dojo():
    if request.method == "POST":
        data = {
            'name' : request.form["name"],
        }
        Dojos.save_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def dojos_ninjas(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo_with_ninjas = Ninjas.get_ninjas_in_dojo(data)
    return render_template('ninjas.html', dojo_with_ninjas = dojo_with_ninjas)

@app.route('/ninja_form')
def ninja_form():
    all_dojos = Dojos.get_all_dojos()
    return render_template("create_ninja.html", all_dojos = all_dojos)

@app.route('/create_ninja', methods = ['GET', 'POST'])
def create_ninja():
    if request.method == "POST":
        ninja_info = {
            'first_name' : request.form["first_name"],
            'last_name' : request.form["last_name"],
            'age' : request.form["age"],
            'dojo_id' : request.form["dojo_id"],
        }
        Ninjas.save_ninjas(ninja_info)
    return redirect('/')