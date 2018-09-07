from flask import Flask
from . import main
from config import config_options
# from .config import DevConfig
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    # initialising flask extension
    app = Flask(__name__)

    #initialising bootstrap
   # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile("config.py")

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
