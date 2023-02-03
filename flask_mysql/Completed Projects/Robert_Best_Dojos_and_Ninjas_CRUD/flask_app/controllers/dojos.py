from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def r_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)


#route for creating a new dojo on the home page
@app.route('/home/new', methods = ["POST"])
def f_new():
    data = {
        "name": request.form["name"]
    }
    Dojo.create(data)
    return redirect('/')

#show dojo
@app.route ('/dojos/show/<int:id>')
def r_show_dojo(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojos_with_ninjas(data)
    return render_template("show_dojo.html", dojo = dojo)

