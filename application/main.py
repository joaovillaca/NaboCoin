from flask.wrappers import JSONMixin
from application import app
from application.blockchain import blockchain
from flask import render_template, redirect, url_for, request, session, flash
from application.forms import RegistrationForm
from werkzeug.wrappers import UserAgentMixin
import json

@app.route('/')
def home():
    message = "Últimos blocos da Nabocoin:"
    action = get_chain()

    return render_template('index.html', action=action, message=message)

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})


@app.route('/buy')
def comprar():
    message = "Compre Nabocoins!"
    action ="Comprar"
    return render_template('index.html', action=action, message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    action ="Cadastro"

    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = UserAgentMixin(form.username.data, form.email.data, form.password.data)
        flash('Thanks for registering' + ' ' + user)
        return redirect(url_for('login'))

    return render_template('forms.html', action=action, form=form)


@app.route('/login')
def login():
    action ="Login"

    if request.method == "POST":
        user = request.form["login"]
        session["user"] = user
        return redirect(url_for("user"))

    return render_template('index.html', action=action)


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.hmtl")
    else:
        return redirect(url_for("login"), user=user)

# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'