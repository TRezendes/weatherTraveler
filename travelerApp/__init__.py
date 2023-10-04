from flask import Flask, render_template, url_for, redirect, request, session
from rikeripsum.rikeripsum import generate_paragraph as RikerIpsum
from pyowm.utils.config import get_config_from
from flask_sqlalchemy import SQLAlchemy
from pyowm import OWM
import response
import json

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    
    with open('flask_config.json') as config_file:
        config = json.load(config_file)

    # General configuration
    app.config['SECRET_KEY'] = config.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DEV_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('SQLALCHEMY_TRACK_MODIFICATIONS')  
    app.config['OWM_API_KEY'] = config.get('OWM_API_KEY')

    db.init_app(app)
    db.app = app

    owm_api_key = app.config['OWM_API_KEY']
    session['owm_key'] = owm_api_key

    gmaps_api_key = app.config['OWM_API_KEY']
    session['gm_key'] = gmaps_api_key
    
    owm_config_dict = get_config_from('owm_config.json')
    owm = OWM(owm_api_key,owm_config_dict)


    
    app.jinja_env.add_extension('jinja2.ext.do')


    with app.app_context():
        # Register blueprints
        from .weather import weather as weather
        app.register_blueprint(weather, url_prefix='/weather')

    # Add RikerIpsum template global
    @app.template_global('RikerIpsum')
    def riker_ipsum(sentences):
        return RikerIpsum(sentences)
    
    # Is this thing on?
    @app.route('/232')
    def its_alive():
        return render_template('itsAlive.html')

    @app.route('/page_check/<page>')
    def page_check(page):
        return render_template(page)

    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/favicon-folder/<icon>')
    def favicon():
        return redirect(url_for('static', filename='images/favicon-folder/<icon>'))



    return app
