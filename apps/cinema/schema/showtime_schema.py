
from apps.cinema import api
from flask_restplus import fields

showtimes_schema = api.model('ShowTime', {
    'id': fields.Integer(required=True),
    'show_date_time': fields.String(required=True),
    'movie': fields.String(required=True),
    'price': fields.Integer(required=True),
    'cinemahall': fields.String(required=True),
    'available_seats': fields.String()
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
    'required': ['show_date_time', 'movie_id', 'price','cinema_hall']
}

