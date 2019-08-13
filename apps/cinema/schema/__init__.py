from .schema_utils import validate_date


from webargs import fields as flds


def param(func):
    return flds.Nested({"operator": flds.Str(required=True), "field": flds.Str(required=True), "value": func})
