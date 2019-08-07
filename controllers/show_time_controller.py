
import os

from models import ShowTime

from .sql_controllers import SQLBaseController

from sql import get_cte_query


class ShowTimeController(SQLBaseController):
    table = ShowTime
    query = 'query'

    def findall(self):
        results = self.db.execute(self.get_query(), named=True, commit=True)
        return results

    def find(self, showtime_id):
        item = f'where id ={showtime_id}'
        results = self.db.execute(
            self.get_query(item), named=True, commit=True)
        return results

    def get_query(self, item=''):
        """
        Query to filter though the sub table from the cte
        """
        return get_cte_query(self.query)+'''select string_agg(distinct seat_number, ',') as available_seats,
            id,movie,price,show_date_time, cinemahall
            from seats 
            {0} 
            group by id,movie,price,show_date_time,cinemahall
            '''.format(item)
