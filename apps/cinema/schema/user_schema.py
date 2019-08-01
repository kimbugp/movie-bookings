from apps.cinema import api
from flask_restplus import fields

user_schema = api.model('Model', {
    'email': fields.String(),
    'password': fields.String,
    'name': fields.String
})
