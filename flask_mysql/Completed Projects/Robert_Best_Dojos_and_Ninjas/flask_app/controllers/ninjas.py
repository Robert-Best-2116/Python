from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.dojo import Dojo

#create ninja page
@app.route('/ninjas/create')
def r_create_ninja():
    return render_template ('create_ninja.html', dojos = dojo.Dojo.get_all())

#create ninja form
@app.route('/ninjas/create/new', methods = ['POST'])
def f_create_ninja():

    id = request.form['dojo_id']
#so i used the data format instead, and it worked for the other section, but not here, so i dont know why that was such an issue
# i dont normally do it this way, i also corrected issues inside of the ninja model that where it wasent connecting to the right DB 
    ninja.Ninja.create_ninja(request.form)
    return redirect (f'/dojos/show/{id}')
    #not sure how to get it to pass to the proper show form. 



#update ninja form
@app.route('/ninjas/update/<int:id>')
def r_ninjas_update(id):
    data = {
        'id' : id
    }
    return render_template ("update_ninja.html", ninja = ninja.Ninja.get_one(data), dojos = dojo.Dojo.get_all())


@app.route('/ninjas/update', methods = ['POST'])
def f_ninjas_update():
    id = request.form['dojo_id']
    ninja.Ninja.update(request.form)
    return redirect (f'/dojos/show/{id}')


#delete function
@app.route('/ninja/delete/<int:id>')
def ninja_delete(id):
    data = {
        'id' : id
    }
    # id = Dojo.get_dojos_with_ninjas(id)
    ninja.Ninja.delete(data)
    id = session['dojo_id']
    return redirect (f'/dojos/show/{id}')
    #return render_template("show_dojo.html", dojo = dojo)
