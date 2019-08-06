
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
