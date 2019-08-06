
from flask import current_app

from apps.middlewares.validation import ValidationError


class SQLBaseController():
    table = 'users'

    def __init__(self, cursor=None):
        self.db = current_app.db
        self.instance = self.table()

    def insert(self, **kwargs):
        query = self.instance.insert_query(kwargs)
        results = self.db.execute(query, named=True, commit=True)
        return results[0]

    def find(self, **kwargs):
        query = self.instance.find('OR', **kwargs)
        return self.db.execute(query, True)

    def find_one(self, **kwargs):
        item = self.find(**kwargs)
        return item[0] if len(item) > 0 else []
