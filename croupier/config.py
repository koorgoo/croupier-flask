import os

curdir = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(curdir)

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/croupier.db'.format(BASE_DIR)
