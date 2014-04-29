from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('croupier.config')

db = SQLAlchemy(app)

api = Api(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
