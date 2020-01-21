import re

from webargs import core
from webargs.flaskparser import FlaskParser
from functools import wraps

suffix = {"ne": "!=", "gt": ">", "gte": ">=", "lt": "<", "lte": "<=", "eq": "="}


param_regex = re.compile(r"(^[a-zA-Z]+[_]?[a-zA-Z]+)|(gt|lt|lte|eq|ne|gte)\b")


class CustomParamsParser(FlaskParser):
    def parse_querystring(self, req, name, field):
        return core.get_value(_structure_dict(req.args), name, field)


def _structure_dict(dict_):
    def structure_dict_pair(r, key, value):
        m = param_regex.findall(key)
        operator = "eq"
        if m:
            ((col, *_), *t) = m
            if t:
                (*_, (*_, operator)) = t
            if r.get(col) is None:
                r[col] = {
                    "operator": [suffix.get(operator)],
                    "value": value,
                    "field": col,
                }
            else:
                r[col]["operator"].append(suffix.get(operator))

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
