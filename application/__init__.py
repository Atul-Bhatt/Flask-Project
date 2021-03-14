# importing the Flask class

from flask import Flask

# Passing the name of the current module to create a Flask object
app = Flask(__name__)

from application import routes
