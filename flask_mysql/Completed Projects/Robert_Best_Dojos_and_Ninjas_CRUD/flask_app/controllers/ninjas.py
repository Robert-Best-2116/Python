from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja


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
    return redirect (f'/dojos/show/{id}' )
