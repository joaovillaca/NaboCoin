from flask import render_template
import json
from application import app
from application.blockchain import blockchain

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})


@app.route('/')
def home():
    message = "Últimos blocos da blockchain:"
    action = get_chain()
    return render_template('index.html',action=action,message=message)


@app.route('/buy')
def comprar():
    action ="Comprar"
    return render_template('index.html',action=action)


@app.route('/login')
def login():
    action ="Login"
    return render_template('index.html',action=action)


@app.route('/register')
def register():
    action ="Cadastro"
    return render_template('index.html',action=action)


# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting (also knows as XSS) and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'