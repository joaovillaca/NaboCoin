from flask import render_template, abort, redirect, url_for
from flask.blueprints import Blueprint
from flask.globals import session
from jinja2 import TemplateNotFound

userpage = Blueprint('userpage', __name__, template_folder='templates')

@userpage.route("/user")
def user():
    if "user" in session:
        user = session["user"]

        try:
            return render_template("user.hmtl")
        except TemplateNotFound:
            abort(404)
    else:
        user = None
        try:
            return redirect(url_for("loginpage.login"))
        except TemplateNotFound:
            abort(404)