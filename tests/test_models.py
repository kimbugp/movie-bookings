import psycopg2

from models.todo import Todo

from .basetest import BaseTestCase


class TestModels(BaseTestCase):

    def test_creating_a_table(self):
        with self.assertRaises(psycopg2.ProgrammingError):
            string = Todo.create()
            self.db.execute(string, commit=False)
