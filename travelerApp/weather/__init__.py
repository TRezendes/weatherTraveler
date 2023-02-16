from flask import Blueprint

games = Blueprint('weather', __name__, template_folder='templates', static_folder='static')

from . import weather_routes
