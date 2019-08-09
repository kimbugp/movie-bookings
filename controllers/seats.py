
from models import Seat

from .sql_controllers import SQLBaseController


class SeatController(SQLBaseController):
    table = Seat
