
class ShowTimeController(SQLBaseController):

    def findall(self):
        query = '''SELECT distinct showtime.id, showtime.show_date_time,movie.name movie,cinemahall.name as cinema_hall,\
            --get unoccopied seats\
            (select string_agg(distinct seat.seat_number, ',') from seat\
            left join ticket on ticket.seat_number = seat.seat_number\
            left join showtime on showtime.cinema_hall = seat.cinema_hall\
            where ticket.showtime_id is null) as seats\

            from showtime\
            inner join movie on showtime.movie_id=movie.id\
            inner join cinemahall on showtime.cinema_hall = cinemahall.id\
            inner join seat on seat.cinema_hall = cinemahall.id\
            order by showtime.show_date_time, cinema_hall\
            '''
