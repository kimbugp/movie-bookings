from models import Ticket
from flask import current_app

from .sql_controllers import SQLBaseController


class UserController(SQLBaseController):

    def insert(self, **kwargs):
        query = '''
        INSERT into users (email, password, name) VALUES \
            ('{email}','{password}','{name}') RETURNING *
        '''.format(**kwargs)
        results = self.db.execute(query, True)
        return {results}
