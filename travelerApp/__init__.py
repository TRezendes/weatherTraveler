from flask import Flask, render_template, url_for, redirect, request
from rikeripsum.rikeripsum import generate_paragraph as RikerIpsum
from flask_sqlalchemy import SQLAlchemy
import response
import json

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    #config = app.config.from_pyfile('../config.py')
    with open('/Users/trezendes/Projects/theadhdmdotcom/config.json') as config_file:
        config = json.load(config_file)

    # General configuration
    app.config['SECRET_KEY'] = config.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DEV_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('SQLALCHEMY_TRACK_MODIFICATIONS')  

    db.init_app(app)
    db.app = app
    
    app.jinja_env.add_extension('jinja2.ext.do')


    with app.app_context():
        # Register blueprints
        from .weather import weather as weather
        app.register_blueprint(weather, url_prefix='/primary')

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
