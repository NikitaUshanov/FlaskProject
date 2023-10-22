from flask import request, redirect, url_for, render_template
from flask_login import login_user
from werkzeug.security import generate_password_hash
from app.register import bp
from app.models.models import User
from app.extensions import db


@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/register", methods=["POST"])
def register_post():
    email = request.form.get("email")
    password = request.form.get("password")

    user = db.session.query(User).filter_by(email=email).first()

    if user:
        return redirect(url_for("register.register"))

    new_user = User(email=email, password=generate_password_hash(password, method="sha256"))

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect(url_for("main.main"))
