from flask import render_template
from flask.helpers import flash
from flask.wrappers import Request
from werkzeug.wrappers import UserAgentMixin
from application import app
from application.blockchain import blockchain
from application.forms import RegistrationForm
import json

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

@app.route('/')
def home():
    message = "Últimos blocos da Nabocoin:"
    action = get_chain()
    return render_template('index.html',action=action,message=message)

@app.route('/buy')
def comprar():
    action ="Comprar"
    return render_template('index.html', action=action)

@app.route('/login')
def login():
    action ="Login"
    return render_template('index.html',action=action)

@app.route('/register', methods=['GET', 'POST'])
def register():
    action ="Cadastro"
    form = RegistrationForm()
    if Request.method == 'POST' and form.validate():
        user = UserAgentMixin(form.username.data, form.email.data,
                    form.password.data)
        flash('Thanks for registering' + ' ' + user)
        return redirect(url_for('login'))
    return render_template('register.html', action=action, form=form)

# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting (also knows as XSS) and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'