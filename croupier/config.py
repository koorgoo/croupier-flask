import os

FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

curdir = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(curdir)

DEBUG = FLASK_ENV == 'development'

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'local')

if FLASK_ENV == 'test':
  SQLALCHEMY_DATABASE_URI = 'sqlite://'  # :memory:
else:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/croupier.db'.format(BASE_DIR)
