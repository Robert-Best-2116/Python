from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def show_user_profile(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{num * word}"






if __name__ == "__main__":

    app.run(debug=True)