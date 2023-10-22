from flask import render_template
from app.main import bp


@bp.route("/")
def main():
    return render_template("index.html")
