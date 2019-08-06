from flask import current_app

from models import Ticket, Users

from .sql_controllers import SQLBaseController


class UserController(SQLBaseController):
    table = Users