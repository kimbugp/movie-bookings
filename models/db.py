import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    def __init__(self, db, auto_commit=False,*args, **kwargs):
        self.connect(db,auto_commit)
    
    def connect(self,db,auto_commit):
        try:
            self.conn = psycopg2.connect(db)
            self.conn.autocommit = auto_commit
        except psycopg2.OperationalError as error:
            raise error
    
    def execute(self, query,commit):
        cur = self.dict_cursor
        results = cur.execute(query)
        cur.close()
        if commit:
            self.conn.commit()
        return results
    
    @property
    def cursor(self):
        return self.conn.cursor()

    @property
    def dict_cursor(self):
        return self.conn.cursor(
            cursor_factory=RealDictCursor)
