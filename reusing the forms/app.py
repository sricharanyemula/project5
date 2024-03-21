from flask import Flask, render_template, request

app = Flask(__name__)

#--------------home page-----------------------------------------
@app.route('/', methods=['GET'])
def homepage():
    return render_template('response.html', message = "Your in home page")

#-------------- adding -----------------------------------------
@app.route('/sub', methods=['GET'])
def subtraction():
    return render_template('form.html', path="/subtraction-form")

@app.route('/subtraction-form', methods=['POST'])
def subtraction_form():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    return render_template('response.html', message=f'subtraction of {num1} and {num2} is {int(num1)-int(num2)}')

#---------------multiplicationj-------------------------
@app.route('/mul', methods=['GET'])
def mul():
    return render_template('form.html', path="/multiplication-form")

@app.route('/multiplication-form', methods=['POST'])
def multiplication():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    result = f'multiplication of {num1} and {num2} is {int(num1)*int(num2)}'
    return render_template('response.html', message=result)
#---------------division-------------------------
@app.route('/div', methods=['GET'])
def div():
    return render_template('form.html', path="/division-form")

@app.route('/division-form', methods=['POST'])
def division():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    result = f'divions of {num1} and {num2} is {int(num1)/int(num2)}'
    return render_template('response.html', message=result)
app.run()