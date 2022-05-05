from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mission')
def mision():
    return render_template('./mission.html')

@app.route('/contactus/<int:num>')
def contactus(num):
    return f'Contact {num}'

@app.route('/register')
def form():
    return render_template('form.html')

@app.route('/registerUser', methods = ['POST'])
def formPost():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'{name} Registered with email {email}'
    else:
        return 'User not registered'


if __name__ == "__main__" :
    app.run(port=3080, debug = True)