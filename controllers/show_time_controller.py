
from models import ShowTime

from .sql_controllers import SQLBaseController


class ShowTimeController(SQLBaseController):
    table = ShowTime

    def findall(self):
        results = self.db.execute(self.get_query(), named=True, commit=True)
        return results

    def find(self, showtime_id):
        item = f'and st.id ={showtime_id}'
        results = self.db.execute(
            self.get_query(item), named=True, commit=True)
        return results

    def get_query(self, item=''):
        return '''select st.id,CAST(st.show_date_time as varchar),
            string_agg(distinct s.seat_number, ',') as available_seats,
            c.name cinemahall,movie.name movie, st.price
            from showtime st
            inner join cinemahall c on c.id = st.cinema_hall
            left join ticket t on t.showtime_id = st.id
            left join seat s on s.cinema_hall = st.cinema_hall
            join movie on movie.id = st.movie_id
            where t.showtime_id is null and st.show_date_time> current_date {0}
            group by s.cinema_hall, cinemahall,t.user_id, st.show_date_time ,movie, st.id
            order by st.show_date_time asc
            '''.format(item)
