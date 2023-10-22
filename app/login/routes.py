from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from app.extensions import db
from app.models.models import User
from app.login import bp


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = db.session.query(User).filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for("login.login"))

    login_user(user, remember=remember)
    return redirect(url_for("main.main"))


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.main"))
