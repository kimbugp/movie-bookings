
from apps.cinema import api
from flask_restplus import fields

from .movie_schema import movie_response_schema
from .cinema_schema import cinema_response_schema

seats_schema = api.model('Seats', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'number': fields.String(required=True),
    'cinema_hall': fields.Integer(required=True),
})

showtimes_schema = api.model('ShowTime', {
    'id': fields.Integer(required=True),
    'show_date_time': fields.String(required=True),
    'movie': fields.Nested(movie_response_schema),
    'price': fields.Integer(required=True),
    'cinemahall': fields.Nested(cinema_response_schema),
    'available_seats': fields.Nested(seats_schema),
    "number_of_seats":fields.Integer(required=True),
})

schema = {
    'type': 'object',
    'properties': {
        'show_date_time': {"allOf": [
            {"type": "string"},
            {"format": "date-time"}
        ]},
        'movie_id': {"allOf": [
            {"type": "integer"},
        ]},
        'price': {"allOf": [
            {"type": "number"},
        ]},
        'cinema_hall': {"allOf": [
            {"type": "integer"}
        ]},
    },
    'required': ['show_date_time', 'movie_id', 'price', 'cinema_hall'],
    'additionalProperties': False
}
