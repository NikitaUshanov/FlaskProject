from flask import Blueprint

bp = Blueprint("machine", __name__)

from app.machine import routes
