#página principal que invoca o método get_chain()

from flask import render_template, abort
from application.api.dump import get_chain
from flask.blueprints import Blueprint
from jinja2 import TemplateNotFound

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route('/', methods=['GET'])
def home():
    message = "Últimos blocos da Nabocoin:"
    #obtém as transações do kafka
    transactions = get_chain()

    try:
        return render_template('index.html', transactions=transactions)
    except TemplateNotFound:
        abort(404)