from flask import Flask

from config import configurations
from database import Connection
from flask_restplus import Api
from views.todo import todo

authorizations = {
    "Bearer Token": {"type": "apiKey", "in": "header", "name": "Authorization"}
}
api = Api(prefix="/api/v1", doc="/docs")


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configurations.get(config, "development"))

    # initialise flask restplus routes
    api.init_app(app, authorizations=authorizations)

    app.register_blueprint(todo)

    db = Connection(app.config.get("DATABASE_URL"))
    app.db = db

    # import views
    import apps.cinema.views

    return app, db
