from flask import Flask
from application.pages.home import homepage
from application.pages.login import loginpage
from application.pages.register import registerpage
from application.pages.user import userpage
from application.pages.buy import buypage
from application.api.dump import blockchain_json_dump

app = Flask(__name__, template_folder='templates')

# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'


app.register_blueprint(homepage)
app.register_blueprint(loginpage)
app.register_blueprint(registerpage)
app.register_blueprint(userpage)
app.register_blueprint(buypage)
app.register_blueprint(blockchain_json_dump)
