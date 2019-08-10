import jsonschema
from datetime import datetime
from apps.middlewares.validation import ValidationError


def validate_json(var, schema):
    try:
        jsonschema.validate(var, schema)
    except Exception as error:
        raise ValidationError('error', payload={'message': error.message})


def validate_date(obj):
    try:
        date = datetime.strptime(obj, "%Y-%m-%d")
    except Exception as error:
        raise ValidationError(
            'error', payload={'message': 'use datetime format YYYY-MM-DD'})
    return True
