import psycopg2

from utils import create_tables

from .basetest import BaseTestCase


class TestModels(BaseTestCase):

    def test_creating_a_table_succeeds(self):
        self.create_tables()

    def create_tables(self):
        create_tables(self.db)
