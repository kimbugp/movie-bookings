from models import *


class NotFound(Exception):
    pass


def create_tables(db):
    tables = [Users, CinemaHall, Movie, ShowTime, Seat, Ticket]
    for table in tables:
        string = table.create()
        with db.cursor(commit=True) as cursor:
            cursor.execute(string)
