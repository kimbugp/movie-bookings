import json

import psycopg2
from unittest.mock import patch
from .basetest import BaseTestCase


class TestShowTime():

    def test_create_showtime_fails_with_no_authentication(self, test_client):
        data = json.dumps({
            "email": "simonp@bb.com",
            "name": "string",
            "password": "string"
        })
        response = test_client.post(
            '/api/v1/showtime', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_create_showtime_with_no_permissions_fails(self, test_client):
        response = test_client.post(
            '/api/v1/showtime')
        assert response.status_code == 401

    def test_create_showtime_succeeds(self, test_client, auth_header):
        data = json.dumps({
            "show_date_time": "2019-11-09 24:00:00",
            "movie_id": 1,
            "price": 20000,
            "cinema_hall": 1
        })
        response = test_client.post(
            '/api/v1/showtime', data=data, headers=auth_header)
        assert response.status_code == 201
