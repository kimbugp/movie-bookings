from flask import Flask

from apps import cinema_app
from config import configurations
from database import Connection
from flask_restplus import Api
from views.todo import todo

api = Api(cinema_app)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config, 'development'))
    app.register_blueprint(todo)
    app.register_blueprint(cinema_app)

    db = Connection(app.config.get('DATABASE_URL'))
    app.db = db

    # import views
    import apps.cinema.views

    return app, db
