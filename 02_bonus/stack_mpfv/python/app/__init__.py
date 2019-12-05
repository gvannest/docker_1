import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + os.environ.get('APP_MONGO_USER', 'user') + ':' + os.environ.get('APP_MONGO_PASS', 'pass') + '@' + os.environ.get('MONGO_HOST', 'mongodb') + ':' + os.environ.get('MONGO_PORT', '27017') + '/' + os.environ.get('APP_MONGO_DB', 'app_db')

mongo = PyMongo(app)
db = mongo.db

from app import views
