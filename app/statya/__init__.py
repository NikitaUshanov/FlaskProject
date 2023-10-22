from flask import Blueprint

bp = Blueprint("statya", __name__)

from app.statya import routes
