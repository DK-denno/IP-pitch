from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
# from flask import Flask
# from . import main
# from config import config_options
# from config import DevConfig
# from flask_bootstrap import Bootstrap 




# def create_app(config_name):
#     # initialising flask extension
#     app = Flask(__name__)

#     #initialising bootstrap
   
#     bootstrap = Bootstrap(app)

#     app.config.from_object(DevConfig)
#     app.config.from_pyfile("config.py")

#     app.config.from_object(config_options[config_name])
#     # config_options[config_name].init_app(app)
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app
