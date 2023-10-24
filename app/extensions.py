from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_migrate import Migrate
from flask_alchemydumps import AlchemyDumps

db = SQLAlchemy()
babel = Babel()
migrate = Migrate()
dumps = AlchemyDumps()
