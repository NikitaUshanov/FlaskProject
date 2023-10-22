from flask import Flask
from flask_login import LoginManager

from config import Config
from app.extensions import db
from app.models.models import User


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

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

    from app.statya import bp as statya_bp
    app.register_blueprint(statya_bp)

    return app
