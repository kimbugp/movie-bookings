from flask import Flask

from config import configurations
from models.db import Database
from views.todo import todo
from views.tickets import ticket


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config, 'development'))
    app.register_blueprint(todo)
    app.register_blueprint(ticket)

    db = Database(app.config.get('DATABASE_URL'))
    app.db = db
    
    return app, db
