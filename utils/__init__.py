from collections import OrderedDict, namedtuple

from apps.middlewares.validation import ValidationError
from models import *

from .fixtures import *


class NotFound(Exception):
    pass


tables = [Users, CinemaHall, Movie, ShowTime, Seat, Ticket]


def create_tables(db):
    for table in tables:
        string = table.create()
        with db.cursor(commit=True) as cursor:
            cursor.execute(string)


def dict_to_tuple(table_name, items, serialize):
    return [namedtuple(table_name, item.keys(), rename=False)(*item.values()) if not serialize else namedtuple(table_name, item.keys(), rename=False)(*item.values())._asdict() for item in items]


def find_or_404(db, model, serialize=False, **kwargs):
    query = model.find('OR', **kwargs)
    results = dict_to_tuple(model.__name__, db.execute(
        query, commit=True), serialize)
    if not results:
        message = []
        for item, value in kwargs.items():
            message.append(f"{item} = '{value}'")
        raise ValidationError('error', status_code=404, payload={
                              'message': "{} not found".format(', '.join(message))})
    return results[-1]


def seed_data(db):
    db.drop_all()
    create_tables(db)
    fixtures = OrderedDict({
        'user': Users,
        'cinemahall': CinemaHall,
        'movie': Movie,
        'showtime': ShowTime,
        'seat': Seat,
        'ticket': Ticket,
    })
    for fixture, model in fixtures.items():
        query = model().insert_query(eval(fixture))
        db.execute(query, named=True, commit=True)
