from flask import render_template
from app.register import bp


@bp.route("/register")
def register():
    return render_template("register.html")
