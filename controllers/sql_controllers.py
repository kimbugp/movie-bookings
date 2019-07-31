
from flask import current_app


class SQLBaseController():
    table = 'users'

    def __init__(self, cursor=None):
        self.db = current_app.db

    def insert(self, **kwargs):
        query = '''
        INSERT into {table_name} ({columns}) VALUES ({values})
        '''.format(table_name=self.table,
                   columns=kwargs.keys(),
                   values=kwargs.values())
        cur = self.db.dict_cursor.execute(query)
        return cur.fetchone()
