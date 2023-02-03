from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def route():
    return "HI Please Go To Play"

@app.route('/play')
def play():
    return render_template("index.html", color = 'blue', num = 3)

#forgot variables need to be passed into the argument section of the function.

@app.route('/play/<int:num>')
def playagain(num):
    return render_template("index.html", color = 'blue', num = num)

@app.route('/play/<int:num>/<string:color>')
def playoncemore(color, num):
    return render_template("index.html", color = color, num = num)

if __name__ == "__main__":
    
    app.run(debug=True)


# intintally made 3 div boxes with blue backgrounds, but realised that it wouldent allow me to change the backgrounds or amounts for the other routes, was totally confused on how i could go about adding more boxes if i already had three and i needed to add int variable that jumped the box amount to the given number. also how could i pass in other colors? not really sure, checked solutions file after some time and realised that i needed to make them for loops with already given variables, so like constants in math for system to be simple and not redudant without creating other html files which would just be clunky and over complacated. 

# so on the last one i dont understand why it needs to be string, when you can put anything in there, is it because its a vairable that were passing in??? 