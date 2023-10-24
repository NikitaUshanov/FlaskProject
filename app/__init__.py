from flask import Flask, request, session, redirect
from flask_login import LoginManager

from config import Config
from app.extensions import db, babel, migrate, dumps
from app.models.models import User


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    migrate.init_app(app, db)

    dumps.init_app(app, db)

    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        if request.args.get("language"):
            session["language"] = request.args.get("language")
        return session.get("language", "en")

    @app.before_request
    def before_url():
        session["before_url"] = request.referrer
        try:
            session["language"]
        except KeyError:
            session["language"] = "en"

    @app.route("/language=<language>")
    def set_language(language=None):
        session["language"] = language
        return redirect(session["before_url"])

    login_manager = LoginManager()
    login_manager.login_view = "login.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(int(user_id))

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp)

    from app.register import bp as register_bp
    app.register_blueprint(register_bp)

    from app.machine import bp as machine_bp
    app.register_blueprint(machine_bp)

    from app.article import bp as article_bp
    app.register_blueprint(article_bp)

    return app
