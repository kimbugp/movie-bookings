import json

import psycopg2

from .end_to_end_base import EndToEndBase


class TestAuthentication(EndToEndBase):

    def setUp(self):
        super().setUp()

    def test_registration_succeeds(self):
        data = json.dumps({
            "email": "string@bb.com",
            "name": "string",
            "password": "string"
        })
        response = self.test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)

    def test_registration_with_missing_fields_fails(self):
        data = json.dumps({
            "name": 'dfds'
        })
        response = self.test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_registration_with_invalid_email_fails(self):
        data = json.dumps({
            "name": 'dfds'
        })
        response = self.test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_login_fails_with_non_existing_user(self):
        data = json.dumps({
            "email": "string@bb.com",
            "password": "dsfdsf"
        })
        response = self.test_client.post(
            '/api/v1/login', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_login_succeeds(self):
        data = json.dumps({
            "email": "string@bb.com",
            "name": "string",
            "password": "dsfdsf"
        })
        self.test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/api/v1/login', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
