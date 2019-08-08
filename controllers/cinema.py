import os

from apps.middlewares.validation import ValidationError
from models import CinemaHall, Seat
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController


class CinemaController(SQLBaseController):
    table = CinemaHall
