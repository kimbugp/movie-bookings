
from models import Movie

from .sql_controllers import SQLBaseController


class MovieController(SQLBaseController):
    table = Movie
