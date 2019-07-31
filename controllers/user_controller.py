from models import Ticket
from flask import current_app

from .sql_controllers import SQLBaseController


class UserController(SQLBaseController):

    def insert(self, **kwargs):
        query = '''
        INSERT into users (email, password, name) VALUES ('{email}','{password}','{name}')
        '''.format(**kwargs)
        cur = self.db.dict_cursor.execute(query)
        import pdb; pdb.set_trace()
        return cur.fetchone()
