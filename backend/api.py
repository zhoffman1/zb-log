from flask import Flask, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, User

import os

# create app
app = Flask(__name__)

# TODO: update the origins to reflect React address
CORS(app, origins=["http://127.0.0.1:8080", "http://localhost:8080"])

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'users.db')
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'users.db')

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()

    print('Initialized the database.')

@app.route('/', methods=['GET'])
def home_get():
    return {}

# 
@app.route('/register/', methods=['POST'])
def user_register():
    # Get json request data
    req_data = request.get_json()

    # Check if username already exists
    user_exists = User.query.filter_by(username=req_data["username"]).first()

    # If username exists, return an error code
    if user_exists:
        return {}, 409
    
    # Create new user in the database
    new_user = User(req_data["username"], req_data["password"])
    db.session.add(new_user)
    db.session.commit()

    # Return empty JSON and Created Status Code
    return {}, 201