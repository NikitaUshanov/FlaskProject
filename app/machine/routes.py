from flask import render_template, request
from flask_login import login_required
from app.machine import bp


@bp.route("/machine")
@login_required
def machine():
    return render_template("machine.html")

