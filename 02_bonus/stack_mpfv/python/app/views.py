from app import app, db
from flask import jsonify
from flask import request
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


@app.route('/users')
def addUser():
    _users = db.users.find()

    item = {}
    data = []
    for user in _users:
        item = {
            'id': str(user['_id']),
            'first_name': user['first_name'],
            'last_name': user['last_name'],
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@app.route('/adduser', methods=['GET'])
def createUser():
    fn = request.args.get('firstname')
    ln = request.args.get('lastname')
    item = {
        'first_name': fn,
        'last_name': ln,
    }
    db.users.insert_one(item)

    return jsonify(
        status=True,
        message=f'User {fn} {ln} saved successfully!'
    ), 201
