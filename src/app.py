from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>")
def hello_world(usuario, idade):
    return {
        "usuario": usuario,
        "idade": idade,
    }

@app.route("/bemvindo")
def bem_vindo():
    return {"mensagem": "Bem-vindo ao Flask"}

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

with app.test_request_context():
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario='Lohan', idade=26))