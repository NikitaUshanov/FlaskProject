from flask import render_template
from app.machine import bp


@bp.route("/machine")
def machine():
    return render_template("machine.html")
