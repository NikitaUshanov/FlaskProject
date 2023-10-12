from flask import render_template, redirect, request
from flask_login import user_unauthorized
from app.login import bp


login_url_exceptions = ["/login", "/register"]


@bp.before_request
def unauthorized():
    if user_unauthorized and request.url_rule.rule not in login_url_exceptions:
        redirect("/login")


@bp.route("/login")
def login():
    return render_template("login.html")
