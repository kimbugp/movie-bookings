import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database():
    def __init__(self, db, auto_commit=True, *args, **kwargs):
        self.connect(db, auto_commit)

    def connect(self, db, auto_commit):
        try:
            self.conn = psycopg2.connect(db)
            self.conn.autocommit = auto_commit
        except psycopg2.OperationalError as error:
            raise error

    def execute(self, query, commit=False):
        try:
            cur = self.cursor
            cur.execute(query)
            if commit:
                self.conn.commit()
            return cur
        except psycopg2.DatabaseError as error:
            raise error

    def drop_all(self):
        query = '''SELECT table_schema,table_name FROM information_schema.tables\
             WHERE table_schema = 'public' ORDER BY table_schema,table_name'''
        cur = self.execute(query)
        rows = cur.fetchall()
        [self.execute("drop table " + row[1] + " cascade") for row in rows]

    @property
    def cursor(self):
        return self.conn.cursor()

    @property
    def dict_cursor(self):
        return self.conn.cursor(
            cursor_factory=RealDictCursor)
