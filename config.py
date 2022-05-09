import os
class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST='app/static/photos'

  # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  SUBJECT_PREFIX ='watchlist'
  SENDER_MAIL = 'joyce.njoroge@student.moringaschool.com'

  # simple mde configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  @staticmethod
  def init_app(app):
    pass

class ProdConfig:
  '''
  Production configuration child class
  Args:
    Config: The parent configuration class with General configuration settings
  '''
  uri = os.getenv('DATABASE_URL')
  if uri and uri.startswith('postgres://'):
    uri = uri.replace('postgres://','postgresql://',1)
  SQLALCHEMY_DATABASE_URI=uri

class TestConfig(Config):
  '''
  '''
  # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/watchlist_test'

class DevConfig(Config):
  '''
  Development configuration child class
  Args: 
       Config: The parent configuration class with general configuration settings
  '''
  # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:whalien52@localhost/watchlist'
DEBUG = True

config_options ={
  'development':DevConfig,
  'production':ProdConfig,
  'test' :TestConfig
}  

