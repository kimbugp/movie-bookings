import re

from apps.cinema import api
from apps.middlewares.validation import ValidationError
from flask_restplus import fields
from .seats_schema import seats_schema

ticket_schema = api.model('Ticket', {
    'payment_method': fields.String(required=True),
    'seat_id': fields.String(required=True),
    'showtime_id': fields.Integer(required=True),
})

ticket_response_body = ticket_schema.clone('Ticket', {
    'id': fields.String(required=True),
    'user_id': fields.Integer(required=True),
    'date_created': fields.String(),
    'show_datetime': fields.String(),
    'movie_id': fields.Integer(),
    'price': fields.Float(),
})


schema = {
    'type': 'object',
    'properties': {
        'payment_method': {"allOf": [
            {"type": "string"},
            {"minLength": 5},
            {"maxLength": 10}
        ]},
        'seat_id': {"allOf":
                    [{"type": ["integer", "array"],
                      "uniqueItems": True,
                      "items":{"type": "integer"}
                      }
                     ]
                    },
        'showtime_id': {"allOf": [
            {"type": "integer"},
            {"minLength": 5},
            {"maxLength": 10}
        ]},
    },
    'required': ['payment_method', 'seat_id', 'showtime_id'],
    'additionalProperties': False
}


def process_tickets_seats(body, seat_ids):
    return [
        {'payment_method': body.get('payment_method'),
         'seat_id': seat,
         'showtime_id': body.get('showtime_id'),
         'user_id': body.get('user_id')}
        for seat in seat_ids]
