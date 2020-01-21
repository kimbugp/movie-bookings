from apps.cinema import api
from apps.middlewares.validation import ValidationError
from apps.cinema.schema.parser import parser


@api.errorhandler(ValidationError)
def handle_invalid_usage(error):
    return error.to_dict(), error.status_code


@parser.error_handler
def handle_request_parsing_error(
    err, req, schema, error_status_code, error_headers
):
    raise ValidationError("error", payload={**err.messages})
