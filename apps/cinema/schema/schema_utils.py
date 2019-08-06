import jsonschema

from apps.middlewares.validation import ValidationError


def validate_json(var, schema):
    try:
        jsonschema.validate(var, schema)
    except Exception as error:
        raise ValidationError('error', payload={'message': error.message})
