from apps.cinema import api
from flask_restplus import fields

schema = {
    "type": "object",
    "properties": {
        "date_of_release": {
            "type": "string",
            "format": "date-time",
            "pattern": "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))",
        },
        "summary": {
            "allOf": [{"type": "string"}, {"minLength": 5}, {"maxLength": 100}]
        },
        "id": {"allOf": [{"type": "integer"}]},
        "length": {"allOf": [{"type": "string"}, {"format": "date-time"}]},
        "name": {
            "allOf": [{"type": "string"}, {"minLength": 1}, {"maxLength": 100}]
        },
        "category": {
            "allOf": [{"type": "string"}, {"minLength": 1}, {"maxLength": 100}]
        },
        "rating": {
            "allOf": [
                {"type": "integer"},
                {"enum": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            ]
        },
    },
    "required": ["date_of_release", "rating", "name", "length", "category"],
    "additionalProperties": False,
}


movie_response_schema = api.model(
    "ShowTime",
    {
        "id": fields.Integer(required=True),
        "name": fields.String(required=True),
        "date_of_release": fields.String(required=True),
        "length": fields.String(required=True),
        "summary": fields.String(required=True),
        "category": fields.String(required=True),
        "rating": fields.Integer(required=True),
    },
)
