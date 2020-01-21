import psycopg2

from .basetest import BaseTestCase
from utils import NotFound, create_tables


class TestModels(BaseTestCase):
    def test_creating_a_table_succeeds(self, init_db):
        create_tables(init_db)
