from flask import render_template, abort
from application.api.dump import get_chain
from flask.blueprints import Blueprint
from jinja2 import TemplateNotFound

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route('/', methods=['GET'])
def home():
    message = "Últimos blocos da Nabocoin:"
    action = get_chain()

    try:
        return render_template('index.html', action=action, message=message)
    except TemplateNotFound:
        abort(404)