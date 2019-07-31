from flask import Flask

from config import configurations
from models.db import Database
from views.todo import todo
from views.users import auth


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config, 'development'))
    app.register_blueprint(todo)
    app.register_blueprint(auth)

    db = Database(app.config.get('DATABASE_URL'))
    app.db = db
    
    return app, db
