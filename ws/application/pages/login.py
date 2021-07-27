from flask import render_template, abort, redirect, url_for
from flask.blueprints import Blueprint
from flask.globals import request, session
from jinja2 import TemplateNotFound

loginpage = Blueprint('loginpage', __name__, template_folder='templates')

@loginpage.route("/login", methods=['GET', 'POST'])
def login():
    action ="Login"

    if request.method == "POST":
        user = request.form["login"]
        session["user"] = user

        try:
            return redirect(url_for("userpage.user"))
        except TemplateNotFound:
            abort(404)
    try:
        return redirect(url_for("homepage.home"))
    except TemplateNotFound:
        abort(404)