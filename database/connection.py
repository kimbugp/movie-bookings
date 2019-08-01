from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager


class DBConnection():
    def __init__(self, db, *args, **kwargs):
        self.pool = ThreadedConnectionPool(1, 20, db)

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
                if commit:
                    connection.commit()
            finally:
                cursor.close()

    @contextmanager
    def cursor(self, commit=False):
        with self.connect() as connection:
            cursor = connection.cursor()
            try:
                yield cursor
                if commit:
                    connection.commit()
            finally:
                cursor.close()

    def execute(self, query, commit=False):
        with self.cursor(commit=commit) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
        return data

    def drop_all(self):
        query = '''SELECT table_schema,table_name FROM information_schema.tables\
             WHERE table_schema = 'public' ORDER BY table_schema,table_name'''
        rows = self.execute(query)
        with self.cursor(commit=True) as cursor:
            [cursor.execute("drop table " + row[1] + " cascade")
             for row in rows]
