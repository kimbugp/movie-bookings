import re

from webargs import core
from webargs.flaskparser import FlaskParser
from functools import wraps

param_regex = re.compile(r"(^[a-zA-Z]+[_]?[a-zA-Z]+)|(gt|lt)\b")


class CustomParamsParser(FlaskParser):
    operators = ('ne', 'gt', 'gte', 'lt', 'lte', 'eq')
    string = ('contains', 'icontains', 'startswith',
              'istartswith', 'endswith', 'iendswith', 'iexact')

    def parse_querystring(self, req, name, field):
        return core.get_value(_structure_dict(req.args), name, field)


def _structure_dict(dict_):
    def structure_dict_pair(r, key, value):
        m = param_regex.findall(key)
        operator = 'eq'
        if m:
            ((col, *_), *t) = m
            if t:
                (*_, (*_, operator)) = t
            if r.get(col) is None:
                r[col] = {'operator': operator, 'value': value, 'field': col}
    r = {}
    for key, value in dict_.items():
        structure_dict_pair(r, key, value)
    return r


parser = CustomParamsParser()
use_kwargs = parser.use_kwargs


def use_args(fields):

    def decorated(func):
        @wraps(func)
        @parser.use_args(fields)
        def inner(*args, **kwargs):
            *args, params = args
            params = [item for item in params.values()]
            return func(*args, params, **kwargs)
        return inner
    return decorated
