import re

from apps.cinema import api
from apps.middlewares.validation import ValidationError
from flask_restplus import fields

from .schema_utils import validate_json

ticket_schema = api.model('Ticket', {
    'payment_method': fields.String(required=True),
    'seat': fields.String(required=True),
    'showtime_id': fields.Integer(required=True),
})

ticket_response_body = ticket_schema.clone('Ticket', {
    'id': fields.String(required=True),
    'user': fields.String(required=True)
})


schema = {
    'type': 'object',
    'properties': {
        'payment_method': {"allOf": [
            {"type": "string"},
            {"minLength": 5},
        ]},
        'seat': {"allOf": [
            {"type": "string"},
        ]},
        'showtime_id': {"allOf": [
            {"type": "integer"},
            {"minLength": 5}
        ]},
    },
    'required': ['payment_method', 'seat', 'showtime_id']
}
