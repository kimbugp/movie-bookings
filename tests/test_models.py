import psycopg2

from models.todo import Todo
from models.users import Users
from utils import create_tables

from .basetest import BaseTestCase


class TestModels(BaseTestCase):

    def test_creating_a_table_when_already_existing(self):
        self.create_tables()
        with self.assertRaises(psycopg2.ProgrammingError):
            self.create_tables()

    def test_creating_a_table_succeeds(self):
        self.create_tables()

    def create_tables(self):
        create_tables(self.db)
