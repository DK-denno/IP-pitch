import os
class Config:
  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  
class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    

class DevConfig(Config):
    DEBUG = True    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/pitches'
   

config_options = {
'development':DevConfig,
'production':ProdConfig,


}
