from app import app, db
from flask import jsonify
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return jsonify(
                status=True,
                message=f"Hello from {app_name} running in a Docker container behind Nginx, and linked to MongoDB!"
                )

    return "Hello from Flask"


@application.route('/adduser')
def addUser():
    _users = db.users.find()

    item = {}
    data = []
    for user in _users:
        item = {
            'id': str(user['_id']),
            'firstname': user['firstname']
            'lastname': user['lastname']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@application.route('/adduser', methods=['POST'])
def createUser():
    data = request.get_json(force=True)
    item = {
        'firstname': data['firstname']
        'lastname': data['lastname']
    }
    db.users.insert_one(item)

    return jsonify(
        status=True,
        message='User saved successfully!'
    ), 201
