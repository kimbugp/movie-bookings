
from apps.cinema import api
from flask_restplus import fields

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
            "uniqueItems": True,
            "items": {
                "type": "object",
                "required": ["name", "number"],
                "properties":
                {
                    "name": {
                        "uniqueItems": True,
                        "type": "string"
                    },
                    "number": {
                        "type": "array",
                        "uniqueItems": True,
                        "items": {
                            "type": "integer"
                        }
                    }
                }
            }
        }
    }
}


def process_seats(seats, cinema_hall):
    results = []
    for col in seats:
        numbers = col.get('number')
        [results.append({'cinema_hall': cinema_hall, 'number': item,
                         'name': col.get('name'), }) for item in numbers]

    return results
