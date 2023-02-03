from flask import render_template,redirect,request, session, flash
from flask_app import app
from flask_app.models.users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/index')


@app.route('/index')
def dashboard():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        print("not valid")
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        # we redirect to the template with the form.
        return redirect('/index')
    print("valid")
    data ={ 
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    User.save(data)
    session['user_id'] = data
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    print("working")
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_data'] = {
        'id' : user_in_db.id
    }
    #user_in_db.id#, user_in_db.first_name, user_in_db.last_name, user_in_db.email
    # never render on a post!!!
    
    return redirect("/logged_in")

@app.route('/logged_in')
def logged_in():
    if 'user_data' not in session:
        return redirect ('/')
    print('session info', session)
    data = {
        'id' : session['user_data']['id'] # this is done because we need to access the key inside of the dicionary that session has saved. 
    }

    return render_template('logged_in.html', user = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')