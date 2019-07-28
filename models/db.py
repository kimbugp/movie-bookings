import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    def __init__(self, db, *args, **kwargs):
        self.connect(db)
    
    def connect(self,db):
        try:
            self.conn = psycopg2.connect(db)
        except psycopg2.OperationalError as error:
            raise error
    
    @property
    def cursor(self):
        return self.conn.cursor()

    @property
    def dict_cursor(self):
        return self.conn.cursor(
            cursor_factory=RealDictCursor)
