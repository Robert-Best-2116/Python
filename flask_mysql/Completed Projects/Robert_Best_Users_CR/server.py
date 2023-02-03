from flask import Flask, render_template, request, redirect
# import the function that will return an instance of a connection
# import the class from friend.py
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/new')
def new():
    return render_template("create_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')


@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        'id':id
    }
    user = User.get_one(data)
    return render_template("show_user.html", user = user)

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template("update_user.html", user = user)

@app.route('/users/update', methods=['POST'])
def update():
    
    data={
        "id" : request.form['id'],
        "first_name" : request.form['fname'],
        "last_name" : request.form['lname'],
        "email" : request.form['email']
    }
    print(data)
    User.update(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)