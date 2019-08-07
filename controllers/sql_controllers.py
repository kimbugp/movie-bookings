
from flask import current_app
from collections import namedtuple
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

    def find(self, operator='OR', **kwargs):
        query = self.instance.find(operator, **kwargs)
        return self.dict_to_tuple(self.db.execute(query, True))

    def find_one(self, **kwargs):
        items = self.find(**kwargs)
        return items[0] if len(items) > 0 else []
    
    def dict_to_tuple(self,items):
        return [namedtuple(self.table.__name__,item.keys(),rename=False)(*item.values()) for item in items]


