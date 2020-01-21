
from models import Ticket, Users # noqa 

from .sql_controllers import SQLBaseController


class UserController(SQLBaseController):
    table = Users
