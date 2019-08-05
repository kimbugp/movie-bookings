from models import Ticket, ShowTime, Seat

from .sql_controllers import SQLBaseController
from utils import find_or_404


class TicketController(SQLBaseController):
    table = Ticket

    def insert(self, **kwargs):
        self.validate_showtime(kwargs.get('showtime_id'))
        self.validate_seat(kwargs.get('seat'))
        return super().insert(**kwargs)

    def validate_showtime(self, showtime_id):
        return find_or_404(self.db, ShowTime, id=showtime_id)

    def validate_seat(self, seat):
        return find_or_404(self.db, Seat, seat_number=seat)
