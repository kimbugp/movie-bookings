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
        self.assertCountEqual(response.json['ticket'][0], 6)
        self.assertKeys(response.json['ticket'][0], {
                        'payment_method': 'mombile',
                        'seat_id': '1', 'showtime_id': 2,
                        'id': '7',
                        'user_id': 2})

    def test_create_show_time_fails_with_cinema_hall_already_filled(self, test_client, auth_header, ticket):
        _, data = ticket
        response = test_client.post(
            '/api/v1/ticket', data=data, headers=auth_header)
        assert response.status_code == 400

    def test_get_all_ticket(self, test_client, auth_header):
        response = test_client.get(
            '/api/v1/ticket', headers=auth_header)
        self.assertCountEqual(response.json['tickets'], 7)
        self.assertCountEqual(response.json['tickets'][0], 9)
        self.assertKeys(response.json['tickets'][0], {
            'payment_method': 'mm',
            'seat_id': '1',
            'showtime_id': 1,
            'id': '1',
            'user_id': 1,
            'show_date_time': '2019-08-09 08:00:00',
            'movie_id': 1,
            'price': 20000.0})
        self.assertEqual(response.status_code, 200)

    def test_filter_tickets_by_query_params(self, test_client, auth_header):
        response = test_client.get(
            '/api/v1/ticket?movie_id=1', headers=auth_header)
        self.assertCountEqual(response.json['tickets'], 7)
        self.assertCountEqual(response.json['tickets'][0], 9)
        self.assertKeys(response.json['tickets'][0], {
            'payment_method': 'mm',
            'seat_id': '1',
            'showtime_id': 1,
            'id': '1',
            'user_id': 1,
            'show_date_time': '2019-08-09 08:00:00',
            'movie_id': 1,
            'price': 20000.0})
        self.assertEqual(response.status_code, 200)

    def test_get_ticket_by_id(self, test_client, ticket, auth_header):
        response = test_client.get('/api/v1/ticket/7', headers=auth_header)
        self.assertCountEqual(response.json['ticket'], 9)
        self.assertKeys(response.json['ticket'], {
            'payment_method': 'mombile',
            'seat_id': '1',
            'showtime_id': 2,
            'id': '2',
            'user_id': 2,
            'show_date_time': '2019-08-07 00:00:00',
            'movie_id': 1,
            'price': 30000.0})
        self.assertEqual(response.status_code, 200)


class TestNormalUserTickets(BaseTestCase):
    def test_get_all_user__ticket(self, test_client, user_auth_header):
        response = test_client.get(
            '/api/v1/ticket', headers=user_auth_header)
        self.assertCountEqual(response.json['tickets'], 0)
        self.assertEqual(response.status_code, 200)

    def test_create_bulk_ticket_succeeds(self, test_client, user_auth_header):
        data = json.dumps({
            "payment_method": "mombile",
            "seat_id": [1, 2],
            "showtime_id": 2
        })
        response = test_client.post(
            '/api/v1/ticket', data=data, headers=user_auth_header)
        self.assertEqual(response.status_code, 201)
        self.assertCountEqual(response.json['ticket'][0], 6)
        self.assertKeys(response.json['ticket'][0], {
            'payment_method': 'mombile',
            'seat_id': '1', 'showtime_id': 2,
            'id': '7',
            'user_id': 2})

    def test_create_bulk_ticket_fails_with_invalid_seats(self, test_client, user_auth_header):
        data = json.dumps({
            "payment_method": "mombile",
            "seat_id": [6, 7, 8, 9, 10],
            "showtime_id": 2
        })
        response = test_client.post(
            '/api/v1/ticket', data=data, headers=user_auth_header)
        self.assertEqual(response.status_code, 400)
        self.assertKeys(response.json, {
                        'message': "seat numbers '{6, 7, 8, 9, 10}' in cinema hall not available check available seats for showtime", 'error': 'error'})
