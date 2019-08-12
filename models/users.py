from datetime import datetime

from database import Model as db
from sql import get_cte_query


class Users(db):
    id = db.fields(db.serial(), db.primary())
    date_created = db.fields(db.datetime(auto_add=True))
    email = db.fields(db.string(100), db.unique(), db.not_null(True))
    password = db.fields(db.string(100), db.not_null(True))
    name = db.fields(db.string(100), db.not_null(False))
    is_staff = db.fields(db.boolean(default=False), db.not_null())

    def find(self, operator, joins, kwargs):
        if any('report' in item.values() for item in kwargs):
            dict_={
                'ticket_enddate': datetime.now().strftime("%Y-%m-%d"),
                'ticket_startdate': datetime.now().strftime("%Y-%m-%d"),
                'total':0
            }
            for index ,item in enumerate(list(kwargs)):
                if item.get('field') in ['ticket_enddate', 'ticket_startdate', 'total']:
                    dict_[index][item.get('field')] = item.get('value')
            return get_cte_query('user_filtering').format(**dict_)

        update = []
        for item in kwargs:
            if item.get('field') not in ['ticket_enddate', 'ticket_startdate', 'total', 'report']:
                update.append(item)
        return super().find(operator, joins, update)
