import os

from apps.middlewares.validation import ValidationError
from models import Seat
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController


class SeatController(SQLBaseController):
    table = Seat
