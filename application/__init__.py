# importing the Flask class


from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api

api = Api()

# Passing the name of the current module to create a Flask object
app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api.init_app(app)

from application import routes
