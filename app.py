from flask import Flask, render_template, request, redirect, url_for

# WSGI Application
app = Flask(__name__)

@app.route('/')
def message():
    return "<h1/>Hello, Worlds!</h1>"

@app.route('/welcome')
def welcome():
    return '<h3>Welcome to the Flask tutorials.</h3>'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    if score >= 40:
        return f'<h1><span style="color:green;">Passed!</span> <br>The Score is: {str(score)}</h1>'
    if score < 40:
        return f'<h1><span style="color:red;">Failed!</span> <br>The Score is: {str(score)}</h1>'

@app.route('/calculate', methods = ['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['maths'])
        history = float(request.form['maths'])

        average_marks = (maths + science + history) / 3

        return redirect(url_for('result', score=average_marks)) # redirect with backend

        # return render_template('result.html', results=average_marks) # render the html template


if __name__ == '__main__':
    app.run(debug = True) # "debug=True" only in development environment

