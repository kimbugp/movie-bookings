import json

from .basetest import BaseTestCase


class EndToEndBase(BaseTestCase):

    def setUp(self):
        self.create_app()
        self.test_client = self.app.test_client()
        self.app.testing = True
        self.create_tables()
