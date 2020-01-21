from .schema_utils import validate_date  # noqa


from webargs import fields as flds


def param(func):
    return flds.Nested(
        {
            "operator": flds.List(flds.Str(required=True), required=True),
            "field": flds.Str(required=True),
            "value": func,
        }
    )
