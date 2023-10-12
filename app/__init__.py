from flask import Flask
from flask_login import LoginManager

from config import Config
from app.extensions import db
from app.models.user import User


def create_app(config_class=Config):
    app = Flask(__name__)
    login_manager = LoginManager()
    app.config.from_object(config_class)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login.login"

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp)

    from app.register import bp as register_bp
    app.register_blueprint(register_bp)

    return app
