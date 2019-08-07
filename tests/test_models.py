import psycopg2

from .basetest import BaseTestCase
from utils import NotFound, create_tables


class TestModels(BaseTestCase):

    def test_creating_a_table_succeeds(self):
        create_tables(self.db)
