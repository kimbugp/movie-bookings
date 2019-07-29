import json

from .basetest import BaseTestCase


class TestTickets(BaseTestCase):

    def setUp(self):
        self.create_app()
        self.test_client = self.app.test_client()
        self.app.testing = True
        self.create_tables()

    def test_create_ticket_succeeds(self):
        data = json.dumps({
            'seat': 'Go for lunch',
            'showtime_id': '100',
            'payment_method': 'mm'
        })
        response = self.test_client.post(
            '/ticket', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
