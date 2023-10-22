from flask import render_template
from app.statya import bp


@bp.route("/statya")
def statya():
    return render_template("statya.html")
