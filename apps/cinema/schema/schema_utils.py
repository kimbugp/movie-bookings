from datetime import datetime


from apps.middlewares.validation import ValidationError


def validate_date(obj):
    try:
        datetime.strptime(obj, "%Y-%m-%d")
    except Exception:
        raise ValidationError(
            "error", payload={"message": "use datetime format YYYY-MM-DD"}
        )
    return True
