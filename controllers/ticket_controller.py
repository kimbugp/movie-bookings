from apps.middlewares.validation import ValidationError
from models import Seat, ShowTime, Ticket
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController


class TicketController(SQLBaseController):
    table = Ticket

    def insert(self, seats, showtime_id, seat_id, **kwargs):
        showtime = self.validate_showtime(showtime_id)
        self.validate_seat(set(seat_id), showtime_id)
        return super().insert(seats)

    def validate_showtime(self, showtime):
        return find_or_404(self.db, ShowTime, id=showtime)

    def validate_seat(self, seats, showtime_id):
        query = get_cte_query('available_seats').format(
            showtime_id=showtime_id)
        results = self.db.execute(query, named=False)
        available_seats = [] if results[0][0] is None else results[0][0]
        seat_diff = seats.difference(set(available_seats))
        if seat_diff:
            raise ValidationError('error', status_code=400, payload={
                'message': f"seat numbers '{seat_diff}' in cinema hall not available check available seats for showtime"})
        return

    def find(self, operator='OR', serialize=False, params=[], **kwargs):
        for index ,item in enumerate(params):
            if item.get('field') in ['show_date_time', 'movie_id', 'price']:
                item['table'] = 'ticket'
        joins = 'left join showtime on showtime.id = ticket.showtime_id'
        return super().find(operator, serialize, joins, params)
