
import os

from models import ShowTime

from .sql_controllers import SQLBaseController

from sql import get_cte_query


class ShowTimeController(SQLBaseController):
    table = ShowTime
    query = 'query'

    def create(self, **kwargs):
        # self.validate_showtime(kwargs)
        import pdb; pdb.set_trace()
        # validate  cinemahall

        # validate movie
        # check where cinemahall will be available for
        # the showtime period given the movie length

        # insert if success
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
