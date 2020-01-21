from apps.cinema import api
from flask_restplus import fields

from .movie_schema import movie_response_schema
from .cinema_schema import cinema_response_schema
from .seats_schema import seats_schema

showtimes_schema = api.model(
    "ShowTime",
    {
        "id": fields.Integer(required=True),
        "show_datetime": fields.String(required=True),
        "movie": fields.Nested(movie_response_schema),
        "price": fields.Integer(required=True),
        "cinemahall": fields.Nested(cinema_response_schema),
        "available_seats": fields.Nested(seats_schema),
        "number_of_seats": fields.Integer(required=True),
    },
)

schema = {
    "type": "object",
    "properties": {
        "show_datetime": {"allOf": [{"type": "string"}, {"format": "date-time"}]},
        "movie_id": {"allOf": [{"type": "integer"}]},
        "price": {"allOf": [{"type": "number"}]},
        "cinema_hall": {"allOf": [{"type": "integer"}]},
    },
    "required": ["show_datetime", "movie_id", "price", "cinema_hall"],
    "additionalProperties": False,
}
