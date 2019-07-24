from unittest import TestCase

from flask import jsonify, make_response

from main import create_app
from utils import NotFound


def raise_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


class BaseTestCase(TestCase):
    def setUp(self):
        self.create_app()
        self.test_client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        self.app_context.pop()

    def create_app(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.register_error_handler(NotFound, raise_not_found)
