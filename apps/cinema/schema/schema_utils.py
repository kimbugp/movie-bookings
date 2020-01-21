from datetime import datetime

import jsonschema

from apps.middlewares.validation import ValidationError


def validate_date(obj):
    try:
        date = datetime.strptime(obj, "%Y-%m-%d")
    except Exception as error:
        raise ValidationError(
            "error", payload={"message": "use datetime format YYYY-MM-DD"}
        )
    return True
