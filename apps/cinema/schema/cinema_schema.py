from apps.cinema import api
from flask_restplus import fields
from .seats_schema import seats_schema

cinema_response_schema = api.model(
    "Cinema",
    {
        "id": fields.Integer(required=True),
        "name": fields.String(required=True),
        "description": fields.String(required=True),
        "seats": fields.Nested(seats_schema),
    },
)

schema = {
    "type": "object",
    "required": ["name", "description", "seats"],
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string", "minLength": 5, "maxLength": 20},
        "description": {
            "type": "string",
            "pattern": "^(.*)$",
            "minLength": 5,
            "maxLength": 100,
        },
        "seats": {
            "type": "array",
            "uniqueItems": True,
            "items": {
                "type": "object",
                "required": ["name", "number"],
                "properties": {
                    "name": {"uniqueItems": True, "type": "string"},
                    "number": {
                        "type": "array",
                        "uniqueItems": True,
                        "items": {"type": "integer"},
                    },
                },
            },
        },
    },
}


def process_seats(seats, cinema_hall):
    results = []
    for col in seats:
        numbers = col.get("number")
        [
            results.append(
                {"cinema_hall": cinema_hall, "number": item, "name": col.get("name")}
            )
            for item in numbers
        ]

    return results
