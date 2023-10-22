from flask import render_template
from flask_login import login_required
from app.article import bp
from app.extensions import db
from app.models.models import Article


@bp.route("/article")
@bp.route("/article/1")
@login_required
def article():
    article = db.session.query(Article).filter_by(id=1).first()
    return render_template("article.html", title=article.title, text=article.text)


@bp.route("/article/<article_id>")
@login_required
def article_n(article_id):
    article = db.session.query(Article).filter_by(id=article_id).first()
    return render_template("article.html", title=article.title, text=article.text)
