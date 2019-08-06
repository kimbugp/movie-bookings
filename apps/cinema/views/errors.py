
from flask import jsonify, make_response

from apps.cinema import api
from apps.middlewares.validation import ValidationError


@api.errorhandler(ValidationError)
def handle_invalid_usage(error):
    return error.to_dict(), error.status_code
