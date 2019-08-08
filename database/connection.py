from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

from apps.middlewares.validation import ValidationError


class DBConnection():
    def __init__(self, db, *args, **kwargs):
        self.pool = ThreadedConnectionPool(1, 20, db)
        self.obj = None

    @contextmanager
    def connect(self):
        try:
            conn = self.pool.getconn()
            yield conn
        finally:
            self.pool.putconn(conn)

    @contextmanager
    def dict_cursor(self, commit=False):
        with self.connect() as connection:
            cursor = connection.cursor(
                cursor_factory=RealDictCursor)
            try:
                yield cursor

            finally:
                if commit:
                    connection.commit()
                cursor.close()

    @contextmanager
    def cursor(self, commit=False):
        with self.connect() as connection:
            cursor = connection.cursor()
            try:
                yield cursor
            finally:
                if commit:
                    connection.commit()
                cursor.close()

    def execute(self, query, named=True, commit=False):
        cur = self.dict_cursor if named else self.cursor
        with cur(commit) as cursor:
            try:
                cursor.execute(query)
                data = list(cursor)
            except(psycopg2.OperationalError, psycopg2.errors.UniqueViolation) as error:
                raise ValidationError(error.args[0].split(
                    'DETAIL:')[1], status_code=400)
            return data

    def drop_all(self):
        query = '''SELECT table_schema,table_name FROM information_schema.tables\
             WHERE table_schema = 'public' ORDER BY table_schema,table_name'''
        rows = self.execute(query, named=False)
        with self.cursor(commit=True) as cursor:
            [cursor.execute("drop table " + row[1] + " cascade")
             for row in rows]
