from models import *
from apps.middlewares.validation import ValidationError


class NotFound(Exception):
    pass


def create_tables(db):
    tables = [Users, CinemaHall, Movie, ShowTime, Seat, Ticket]
    for table in tables:
        string = table.create()
        with db.cursor(commit=True) as cursor:
            cursor.execute(string)


def find_or_404(db, model, **kwargs):
    query = model.find('OR', **kwargs)
    results = db.execute(query, commit=True)
    if not results:
        result = []
        for item, value in kwargs.items():
            result.append(f"{item} = '{value}'")
        raise ValidationError('error', status_code=400, payload={
                              'message': "{} not found".format(', '.join(result))})
    return results
