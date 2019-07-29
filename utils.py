from models import *


class NotFound(Exception):
    pass


def create_tables(db):
    tables = [Users, Todo]
    for table in tables:
        string = table.create()
        db.execute(string, commit=True)
