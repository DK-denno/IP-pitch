import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_PORT = os.environ.get("MAIL_PORT")
  
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    

class DevConfig(Config):
    DEBUG = True    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/pitches'
   

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
