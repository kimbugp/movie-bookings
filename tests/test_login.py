import json

import psycopg2

from .basetest import BaseTestCase


class TestAuthentication(BaseTestCase):

    def test_registration_succeeds(self, test_client):
        data = json.dumps({
            "email": "simonp@bb.com",
            "name": "string",
            "password": "string"
        })
        response = test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 201

    def test_registration_with_missing_fields_fails(self, test_client):
        data = json.dumps({
            "name": 'dfds'
        })
        response = test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 400

    def test_registration_with_invalid_email_fails(self, test_client):
        data = json.dumps({
            "name": 'dfds'
        })
        response = test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 400

    def test_login_fails_with_non_existing_user(self, test_client):
        data = json.dumps({
            "email": "invalid@bb.com",
            "password": "dsfdsf"
        })
        response = test_client.post(
            '/api/v1/login', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_login_succeeds(self, test_client, registration):
        data = json.dumps({
            "email": "string@bb.com",
            "password": "dsfdsf"
        })
        response = test_client.post(
            '/api/v1/login', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 200

    def test_get_current_user(self, auth_header, test_client):
        response = test_client.get(
            '/api/v1/auth', headers=auth_header)
        assert response.status_code == 200
