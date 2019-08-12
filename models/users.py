from database import Model as db

from sql import get_cte_query
from datetime import datetime


class Users(db):
    id = db.fields(db.serial(), db.primary())
    date_created = db.fields(db.datetime(auto_add=True))
    email = db.fields(db.string(100), db.unique(), db.not_null(True))
    password = db.fields(db.string(100), db.not_null(True))
    name = db.fields(db.string(100), db.not_null(False))
    is_staff = db.fields(db.boolean(default=False), db.not_null())

    def find(self, operator, joins='', **kwargs):
        if kwargs.get('report', False):
            kwargs['total'] = kwargs.get('total', 0)
            for item in ['ticket_enddate', 'ticket_startdate']:
                if item not in kwargs.keys():
                    kwargs[item] = datetime.now().strftime("%Y-%m-%d")
            return get_cte_query('user_filtering').format(**kwargs)

        else:
            [kwargs.pop(item, None) for item in list(kwargs) if item in [
                'ticket_enddate', 'ticket_startdate', 'total', 'report']]
        return super().find(operator, joins, **kwargs)
