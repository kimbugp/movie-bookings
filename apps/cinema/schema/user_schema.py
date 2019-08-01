from apps.cinema import api
from flask_restplus import fields

user_schema_fields = api.model('User', {
    'email': fields.String(required=True),
    'name': fields.String(required=True),
    'id': fields.Integer(required=True)
})

user_request_fields = api.model('User', {
    'email': fields.String(required=True),
    'name': fields.String(required=True),
    'password': fields.String(required=True)
})
