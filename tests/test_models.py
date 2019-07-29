import psycopg2

from .basetest import BaseTestCase


class TestModels(BaseTestCase):

    def test_creating_a_table_succeeds(self):
        self.create_tables()
