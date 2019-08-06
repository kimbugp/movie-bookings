from apps.middlewares.validation import ValidationError
from models import Seat, ShowTime, Ticket
from utils import find_or_404

from .sql_controllers import SQLBaseController


class TicketController(SQLBaseController):
    table = Ticket

    def insert(self, **kwargs):
        showtime = self.validate_showtime(kwargs.get('showtime_id'))
        self.validate_seat(kwargs.get('seat_number'),
                           kwargs.get('showtime_id'))
        return super().insert(**kwargs)

    def validate_showtime(self, showtime):
        return find_or_404(self.db, ShowTime, id=showtime)

    def validate_seat(self, seat, showtime_id):
        query = '''select TRUE as result where '{0}' in
                (select distinct seat_number
                    from showtime st
                    right join seat s on  s.cinema_hall = st.cinema_hall
                    where st.id ={1}
                except
                select t.seat_number from
                    ticket t
                    where t.showtime_id = {1})'''.format(seat, showtime_id)
        results = self.db.execute(query, named=True, commit=True)
        if not results:
            raise ValidationError('error', status_code=400, payload={
                'message': f" seat {seat} in cinema_hal not available check available seats for showtime"})
        return results
