from flask import Flask
from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)
CORS(app) # allow CORS