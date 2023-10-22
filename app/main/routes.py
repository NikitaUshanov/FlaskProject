from flask import render_template, session, redirect, url_for, request
from app.main import bp


@bp.route("/")
def main():
    return render_template("index.html")


@bp.route("/language=<language>")
def set_language(language=None):
    session["language"] = language
    return redirect(url_for("main.main"))
