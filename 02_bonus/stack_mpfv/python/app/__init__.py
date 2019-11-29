from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

#app.config["MONGO_URI"] = 'mongodb://' + os.environ['APP_MONGO_USER'] + ':' + os.environ['APP_MONGO_PASS'] + '@' + os.environ['MONGO_HOST'] + ':' + os.environ['MONGO_PORT'] + '/' + os.environ['APP_MONGO_DB']

#mongo = PyMongo(app)
#db = mongo.db

from app import views
