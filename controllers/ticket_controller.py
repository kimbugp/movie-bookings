from models import Ticket
from flask import current_app

from .basecontroller import BaseController


class TicketController(BaseController):
    model = Ticket

    def save(self, *args, **kwargs):
        query = self.model().insert(self.new)
        cur = current_app.db.execute(query, True)
        import pdb; pdb.set_trace()
        cur.fetchone()
