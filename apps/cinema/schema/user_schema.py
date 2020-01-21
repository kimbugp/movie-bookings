import re

from apps.cinema import api
from apps.middlewares.validation import ValidationError
from flask_restplus import fields

user_schema_fields = api.model(
    "User",
    {
        "email": fields.String(required=True),
        "name": fields.String(required=True),
        "id": fields.Integer(required=True),
        "total": fields.Float(),
    },
)

user_request_fields = api.model(
    "User",
    {
        "email": fields.String(required=True),
        "name": fields.String(required=False),
        "password": fields.String(required=True),
    },
)

login_schema = user_schema_fields.clone("User", {"token": fields.String(required=True)})

user_schema = {
    "type": "object",
    "properties": {
        "email": {"allOf": [{"type": "string"}, {"minLength": 5}, {"format": "email"}]},
        "password": {"allOf": [{"type": "string"}, {"minLength": 5}]},
        "name": {"allOf": [{"type": "string"}, {"minLength": 5}]},
        "is_staff": {"allOf": [{"type": "boolean"}]},
    },
    "required": ["email", "password", "name"],
    "additionalProperties": False,
}

user_login_schema = {
    "type": "object",
    "properties": {
        "email": {
            "allOf": [
                {"type": "string"},
                {"minLength": 5},
                {
                    "pattern": "[a-z0-9\\._%+!$&*=^|~#%{}/\\-]+@([a-z0-9\\-]+\\.){1,}([a-z]{2,22})"
                },
            ]
        },
        "password": {"allOf": [{"type": "string"}, {"minLength": 5}]},
    },
    "required": ["email", "password"],
    "additionalProperties": False,
}
