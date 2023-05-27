from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from backend.models import db, User

# create app
app = Flask(__name__)

# TODO: update the origins to reflect React address
CORS(app, origins=["http://127.0.0.1:8080", "http://localhost:8080"])

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

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
    return {}, 201

# @app.route('/login_user/', methods=['POST'])