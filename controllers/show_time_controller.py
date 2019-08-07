
from models import ShowTime

from .sql_controllers import SQLBaseController


class ShowTimeController(SQLBaseController):
    table = ShowTime

    def findall(self):
        results = self.db.execute(self.get_query(), named=True, commit=True)
        return results

    def find(self, showtime_id):
        item = f'where id ={showtime_id}'
        results = self.db.execute(
            self.get_query(item), named=True, commit=True)
        return results

    def get_cte_query(self):
        """
        Common table(cte) expression to get showtime rows including available seats
        """
        return '''
            -- cte for seats , showtime ids, movie name and price
            with seats as (select distinct s.seat_number,st.id as id,m.name movie, st.price, st.show_date_time::varchar,c.name cinemahall
                from showtime st
            --	right join seats to st to get all seats
                right join seat s on  s.cinema_hall = st.cinema_hall
            --	join movie table with st table to get movie name
                inner join movie m on m.id = st.movie_id
            --	join cinema table to get cinema name
                join cinemahall c on c.id = st.cinema_hall
            --	get only showtimes in the future
                where st.show_date_time >now()::date
            except
            -- get seats which are already taken from tickets table
            select t.seat_number,t.showtime_id,NULL,NULL,NULL,NULL
                from 
                ticket t)

            '''

    def get_query(self, item=''):
        """
        Query to filter though the sub table from the cte
        """
        return self.get_cte_query()+'''select string_agg(distinct seat_number, ',') as available_seats,
            id,movie,price,show_date_time, cinemahall
            from seats 
            {0} 
            group by id,movie,price,show_date_time,cinemahall
            '''.format(item)
