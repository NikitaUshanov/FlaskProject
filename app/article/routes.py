from flask import render_template, session
from flask_login import login_required
from app.article import bp
from app.extensions import db
from app.models.models import Article


@bp.route("/article")
@bp.route("/article/1")
@login_required
def article():
    article = db.session.query(Article).filter_by(id=1).first()
    text = article.text_ru if session["language"] == "ru" else article.text_en
    return render_template("article.html", title=article.title, text=text)


@bp.route("/article/<article_id>")
@login_required
def article_n(article_id):
    image = False
    if article_id == "5":
        image = True
    article = db.session.query(Article).filter_by(id=article_id).first()
    text = article.text_ru if session["language"] == "ru" else article.text_en
    return render_template("article.html", title=article.title, text=text, image=image)
