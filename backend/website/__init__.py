from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS 


db = SQLAlchemy()

def create_app(config_override=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config_override:
        app.config.update(config_override)

    db.init_app(app)
    CORS(app)

    from website import models 

    return app

