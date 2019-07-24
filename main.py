from flask import Flask

from config import configurations
from views.todo import todo


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config, 'development'))
    app.register_blueprint(todo)

    return app
