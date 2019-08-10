
from apps.cinema import api
from flask_restplus import fields

seats_schema = api.model('Seats', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'number': fields.String(required=True),
    'cinema_hall': fields.Integer(required=True),
})
