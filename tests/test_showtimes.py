import json

import psycopg2
from unittest.mock import patch
from .end_to_end_base import EndToEndBase


class TestShowTime(EndToEndBase):

    def test_create_showtime_fails_with_no_authentication(self):
        data = json.dumps({
            "email": "simonp@bb.com",
            "name": "string",
            "password": "string"
        })
        response = self.test_client.post(
            '/api/v1/showtime', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_create_showtime_with_no_permissions_fails(self):
        data = json.dumps({
            "email": "simonp@bb.com",
            "name": "string",
            "password": "string"
        })
        response = self.test_client.post(
            '/api/v1/showtime', data=data, headers={'Content-Type': 'application/json',
                                                    'Authorization': self.get_token()})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {
                         'message': 'You have not permission to perform this action', 'error': 'error'})
