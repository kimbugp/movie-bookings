import json

import psycopg2
from .basetest import BaseTestCase


class TestTickets(BaseTestCase):

    def test_create_ticket_fails_with_no_authentication(self, test_client):
        data = json.dumps({
        })
        response = test_client.post(
            '/api/v1/ticket', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_create_cinema_with_no_permissions_fails(self, test_client):
        response = test_client.post(
            '/api/v1/ticket')
        assert response.status_code == 401

    def test_create_ticket_succeeds(self, ticket):
        response, data = ticket
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'ticket':
            [{'payment_method': 'mombile',
              'seat_id': '1',
              'showtime_id': 2,
              'id': '7',
              'user_id': 2}]})

    def test_create_show_time_fails_with_cinema_hall_already_filled(self, test_client, auth_header, ticket):
        _, data = ticket
        response = test_client.post(
            '/api/v1/ticket', data=data, headers=auth_header)
        assert response.status_code == 400

    def test_get_all_ticket(self, test_client, auth_header):
        response = test_client.get(
            '/api/v1/ticket', headers=auth_header)
        self.assertIn(response.json['tickets'], {
                      'payment_method': 'mombile',
                      'seat_id': '1',
                      'showtime_id': 2,
                      'id': '7',
                      'user_id': 2})
        self.assertEqual(response.status_code, 200)

    def test_get_ticket_by_id(self, test_client, ticket, auth_header):
        response = test_client.get('/api/v1/ticket/7', headers=auth_header)
        self.assertEqual(response.json, {
            'tickets':
            {'payment_method': 'mombile',
             'seat_id': '1',
             'showtime_id': 2,
             'id': '7',
             'user_id': 2}})
        self.assertEqual(response.status_code, 200)
