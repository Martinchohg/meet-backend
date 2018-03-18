from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import DBSettings
from flask_cors import CORS, cross_origin

db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    CORS(application)
    application.config.from_object(DBSettings)
    application.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
    application.config['CORS_SUPPORT_CREDENTIALS'] = True
    application.url_map.strict_slashes = False
    global db
    db = SQLAlchemy()
    db.init_app(application)
    return application
