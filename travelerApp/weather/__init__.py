from flask import Blueprint

weather = Blueprint('weather', __name__, template_folder='templates', static_folder='static')

from . import weather_routes
