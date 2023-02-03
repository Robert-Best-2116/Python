from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = "keep it sevret, keep it safe"

@app.route('/')
def index():
    print()

    return render_template("index.html")

@app.route('/student', methods=['POST'])
def create_student():
    print("Information Submitted")
    print(request.form)
    session['studentname'] = request.form['name']
    session['studentlocation'] = request.form['location']
    session['favlanguage'] = request.form['language']
    session['studentcomment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html",
    name_on_template=session['studentname'],
    student_location=session['studentlocation'],
    fav_language=session['favlanguage'],
    student_comment=session['studentcomment']
    )

if __name__ == "__main__":
    app.run(debug=True)