import os

from apps.middlewares.validation import ValidationError

script_dir = os.path.dirname(__file__)


def get_cte_query(file_name):
    file_path = os.path.join(script_dir, f"./{file_name}.sql")
    try:
        with open(file_path, "r") as ofile:
            query = ofile.read()
    except FileNotFoundError as error:
        raise ValidationError(
            message="error", status_code=500, payload={"message": "Unknown error"}
        )
    return query
