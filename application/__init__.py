from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restx import Api
app = Flask(__name__)

api = Api()
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api.init_app(app)
from application import routes