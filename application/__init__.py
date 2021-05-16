from flask import Flask
app = Flask(__name__)

# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting (also knows as XSS) and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'