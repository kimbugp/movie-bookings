
from apps.cinema import api
from flask_restplus import fields

cinema_schema = api.model('ShowTime', {
    'id': fields.Integer(required=True),
    'show_date_time': fields.String(required=True),
    'movie': fields.String(required=True),
    'price': fields.Integer(required=True),
    'cinemahall': fields.String(required=True),
    'available_seats': fields.String()
})

schema = {
    "type": "object",
    "required": ["name", "description", "seats"],
    'additionalProperties': False,
    "properties": {
        "name": {
            "type": "string",
            "minLength": 5,
            "maxLength": 20,
        },
        "description": {
            "type": "string",
            "pattern": "^(.*)$",
            "minLength": 5,
            "maxLength": 100,
        },
        "seats": {
            "type": "array",
            "maxItems": 20,
            "uniqueItems": True,
            "additionalItems": True,
            "items": {
                "type": "string",
                "pattern": "^(.*)$"
            }
        }
    }
}
