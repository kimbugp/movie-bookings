
import os

from apps.middlewares.validation import ValidationError
from models import CinemaHall, Movie, ShowTime
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController


class ShowTimeController(SQLBaseController):
    table = ShowTime
    query = 'query'

    def create(self, **kwargs):
        cinema_hall = find_or_404(
            self.db, CinemaHall, id=kwargs.get('cinema_hall'))

        movie = find_or_404(self.db, Movie, id=kwargs.get('movie_id'))
        # check where cinemahall will be available for
        # the showtime period given the movie length
        if self.db.execute(self.instance.clean(kwargs)):
            raise ValidationError('error', payload={
                                  'message': f"Cinema hall {cinema_hall.name} already occupied for the showtime {kwargs.get('show_date_time')}"})
        return self.insert(**kwargs)

    def findall(self):
        results = self.db.execute(self.get_query(), named=True, commit=True)
        return results

    def find(self, showtime_id):
        item = f'where st.id ={showtime_id}'
        results = self.db.execute(
            self.get_query(item), named=True, commit=True)
        return results

    def get_query(self, item=''):
        """
        Query to filter though the sub table from the cte
        """
        return get_cte_query(self.query).format(item)
