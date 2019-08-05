
from models import ShowTime

from .sql_controllers import SQLBaseController


class ShowTimeController(SQLBaseController):
    table = ShowTime

    def findall(self):
        query = '''select st.id,CAST(st.show_date_time as varchar),
            string_agg(distinct s.seat_number, ',') as seats,
            c.name cinemahall,movie.name movie
            from seat s
            inner join cinemahall c on c.id = s.cinema_hall
            left join ticket t on t.seat_number = s.seat_number
            inner join showtime st on st.cinema_hall = c.id
            join movie on movie.id = st.movie_id
            where t.showtime_id is null and st.show_date_time> current_date
            group by s.cinema_hall, cinemahall,t.user_id, st.show_date_time ,movie, st.id
            order by st.show_date_time asc
            '''
        results = self.db.execute(query, named=True, commit=True)
        return results
