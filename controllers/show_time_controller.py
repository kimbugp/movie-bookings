import os

from apps.middlewares.validation import ValidationError
from models import CinemaHall, Movie, ShowTime
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController
from datetime import datetime


class ShowTimeController(SQLBaseController):
    table = ShowTime
    query = "query"

    def insert(self, kwargs):
        cinema_hall = find_or_404(self.db, CinemaHall, id=kwargs.get("cinema_hall"))

        movie = find_or_404(self.db, Movie, id=kwargs.get("movie_id"))
        # check where cinemahall will be available for
        # the showtime period given the movie length
        if self.db.execute(self.instance.clean(kwargs)):
            raise ValidationError(
                "error",
                payload={
                    "message": f"Cinema hall {cinema_hall.name} already occupied for the showtime {kwargs.get('show_datetime')}"
                },
            )
        return super().insert(kwargs)

    def find(self, operator="AND", serialize=False, joins="", params=[], **kwargs):
        record_id = kwargs.get("id", None)
        start_date = kwargs.get("start_date", datetime.now())
        item = f"where st.id ={record_id}" if record_id else ""
        results = self.db.execute(
            self.get_query(start_date=start_date, item=item), named=True, commit=True
        )
        return results

    def get_query(self, item="", start_date=datetime.now()):
        """
        Query to filter though the sub table from the cte
        """
        return get_cte_query(self.query).format(item, start_date=start_date)
