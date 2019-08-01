from models import Ticket
from flask import current_app

from .sql_controllers import SQLBaseController
from models import Users


class UserController(SQLBaseController):
    table = 'users'

    def insert(self, **kwargs):
        query = '''
        INSERT into {table} (email, password, name) VALUES \
            ('{email}','{password}','{name}') RETURNING *
        '''.format(table=self.table, **kwargs)
        results = self.db.execute(query, named=True, commit=True)
        return results[0]

    def find(self, **kwargs):
        query = Users.find('OR', **kwargs)
        return self.db.execute(query, True)
