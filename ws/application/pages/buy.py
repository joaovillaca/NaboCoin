from flask import render_template, abort, redirect, url_for
from flask.blueprints import Blueprint
from jinja2 import TemplateNotFound

buypage = Blueprint('buypage', __name__, template_folder='templates')

@buypage.route('/buy')
def comprar():
    message = "Compre Nabocoins!"
    action ="Comprar"

    try:
        return render_template('index.html', action=action, message=message)
    except TemplateNotFound:
        abort(404)