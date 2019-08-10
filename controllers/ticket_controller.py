from apps.middlewares.validation import ValidationError
from models import Seat, ShowTime, Ticket
from sql import get_cte_query
from utils import find_or_404

from .sql_controllers import SQLBaseController


class TicketController(SQLBaseController):
    table = Ticket

    def insert(self, kwargs):
        showtime = self.validate_showtime(kwargs.get('showtime_id'))
        self.validate_seat(kwargs.get('seat_id'),
                           kwargs.get('showtime_id'))
        return super().insert(kwargs)

    def validate_showtime(self, showtime):
        return find_or_404(self.db, ShowTime, id=showtime)

    def validate_seat(self, seat, showtime_id):
        query = get_cte_query('available_seats').format(
            seat_id=seat, showtime_id=showtime_id)
        results = self.db.execute(query, named=True, commit=True)
        if not results:
            raise ValidationError('error', status_code=400, payload={
                'message': f" seat number ['{seat}'] in cinema hall not available check available seats for showtime"})
        return results

    def find(self, operator='OR', serialize=False, **kwargs):
        showtime_date = kwargs.pop('showtime_date', None)
        joins = ''
        if showtime_date:
            kwargs['showtime.show_date_time'] = showtime_date
            joins = 'left join showtime on showtime.id = ticket.showtime_id'
        query = self.instance.find(operator, joins, check='>=', ** kwargs)
        return self.dict_to_tuple(self.db.execute(query, True), serialize)
