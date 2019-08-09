import json

import psycopg2
from .basetest import BaseTestCase


class TestCinema():

    def test_create_cinema_fails_with_no_authentication(self, test_client):
        data = json.dumps({
        })
        response = test_client.post(
            '/api/v1/cinema', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_create_cinema_with_no_permissions_fails(self, test_client):
        response = test_client.post(
            '/api/v1/cinema')
        assert response.status_code == 401

    def test_create_cinema_succeeds(self, cinema):
        response, data = cinema
        assert response.status_code == 201

    def test_create_show_time_fails_with_cinema_hall_already_filled(self, test_client, auth_header, cinema):
        _, data = cinema
        response = test_client.post(
            '/api/v1/cinema', data=data, headers=auth_header)
        assert response.status_code == 400
