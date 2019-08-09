import os

from models import CinemaHall

from .sql_controllers import SQLBaseController


class CinemaController(SQLBaseController):
    table = CinemaHall
