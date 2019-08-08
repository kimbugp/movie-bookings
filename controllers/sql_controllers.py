
from collections import namedtuple

from flask import current_app

from apps.middlewares.validation import ValidationError
from utils import dict_to_tuple


class SQLBaseController():
    table = 'users'

    def __init__(self, cursor=None):
        self.db = current_app.db
        self.instance = self.table()

    def insert(self, **kwargs):
        query = self.instance.insert_query(kwargs)
        results = self.db.execute(query, named=True, commit=True)
        return results[0]

    def find(self, operator='OR', serialize=False, **kwargs):
        query = self.instance.find(operator, **kwargs)
        return self.dict_to_tuple(self.db.execute(query, True), serialize)

    def find_one(self, serialize=False, **kwargs):
        items = self.find(serialize=serialize, **kwargs)
        return items[0] if len(items) > 0 else []

    def dict_to_tuple(self, items, serialize):
        return dict_to_tuple(self.table.__name__, items, serialize)
