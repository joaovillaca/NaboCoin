from flask.helpers import flash
from werkzeug.wrappers import UserAgentMixin
from application.utils.forms import RegistrationForm
from flask import render_template, abort, redirect, url_for
from flask.blueprints import Blueprint
from flask.globals import request
from jinja2 import TemplateNotFound

registerpage = Blueprint('registerpage', __name__, template_folder='templates')

@registerpage.route("/register", methods=['GET', 'POST'])
def register():

    action ="Cadastro"
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        user = UserAgentMixin(form.username.data, form.email.data, form.password.data)
        flash('Thanks for registering' + ' ' + user)
        try:
            return redirect(url_for('loginpage.login'))
        except TemplateNotFound:
            abort(404)
    try:
        return render_template('register.html', action=action, form=form)
    except TemplateNotFound:
        abort(404)