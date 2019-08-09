import re

from .schema_utils import validate_json

from apps.cinema import api
from apps.middlewares.validation import ValidationError
from flask_restplus import fields

user_schema_fields = api.model('User', {
    'email': fields.String(required=True),
    'name': fields.String(required=True),
    'id': fields.Integer(required=True)
})

user_request_fields = api.model('User', {
    'email': fields.String(required=True),
    'name': fields.String(required=False),
    'password': fields.String(required=True)
})

login_schema = user_schema_fields.clone('User', {
    'token': fields.String(required=True)
})

user_schema = {
    'type': 'object',
    'properties': {
        'email': {"allOf": [
            {"type": "string"},
            {"minLength": 5},
            {'format': 'email'},
        ]},
        'password': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'name': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'is_staff': {"allOf": [
            {"type": "boolean"},
        ]},
    },
    'required': ['email', 'password', 'name'],
    'additionalProperties': False
}

user_login_schema = {
    'type': 'object',
    'properties': {
        'email':  {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'password': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
    },
    'required': ['email', 'password'],
    'additionalProperties': False
}


def process_user_json(var, partial=False):
    schema = user_schema.copy()
    if partial:
        schema.pop('required')
    validate_json(var, schema)
    if re.match(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', var['email'], re.I):
        return var
    raise ValidationError(
        'error', payload={'message': 'provide a valid email'})


def process_signin_json(var):
    schema = user_login_schema.copy()
    validate_json(var, schema)
