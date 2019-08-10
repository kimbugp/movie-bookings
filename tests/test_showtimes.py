import json

import psycopg2

from .basetest import BaseTestCase


class TestShowTime(BaseTestCase):

    def test_create_showtime_fails_with_no_authentication(self, test_client):
        data = json.dumps({
        })
        response = test_client.post(
            '/api/v1/showtime', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_create_showtime_with_no_permissions_fails(self, test_client):
        response = test_client.post(
            '/api/v1/showtime')
        assert response.status_code == 401

    def test_create_showtime_succeeds(self, showtime):
        response, data = showtime
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['showtimes']
                         ['show_date_time'], '2019-11-10 00:00:00')

    def test_create_showtime_fails_with_not_found_args(self, test_client, auth_header):
        data = json.dumps({
            "show_date_time": "2019-11-09 24:00:00",
            "movie_id": 100,
            "price": 20000,
            "cinema_hall": 1
        })
        response = test_client.post(
            '/api/v1/showtime', data=data, headers=auth_header)
        assert response.status_code == 404

    def test_create_show_time_fails_with_cinema_hall_already_filled(self, test_client, auth_header, showtime):
        _, data = showtime
        response = test_client.post(
            '/api/v1/showtime', data=data, headers=auth_header)
        assert response.status_code == 400

    def test_get_show_time(self, test_client, showtime, auth_header):
        response = test_client.get(
            '/api/v1/showtime', headers=auth_header)
        self.assertEqual(response.json, {
            'showtimes':
            [{'id': 8,
              'show_date_time': '2019-11-10 00:00:00',
              'movie': 'sim', 'price': 20000,
              'cinemahall': 'Cinema1',
              'available_seats': '1-->a1,2-->a2,3-->a3,4-->b2,5-->b4'}]})
        self.assertEqual(response.status_code, 200)

    def test_get_show_time_by_id(self, test_client, showtime, auth_header):
        response = test_client.get(
            '/api/v1/showtime/1'.format(1), headers=auth_header)

        self.assertEqual(response.status_code, 200)

    def test_update_show_time_by_id_with_same_time_slot_fails(self, test_client, showtime, auth_header):
        _, data = showtime
        response = test_client.put(
            '/api/v1/showtime/1', data=data, headers=auth_header)
        assert response.status_code == 400

    def test_update_show_time_by_id_succeeds(self, test_client, showtime, auth_header):
        data = json.dumps({
            "show_date_time": "2019-10-09 24:00:00",
            "movie_id": 1,
            "price": 20000,
            "cinema_hall": 1
        })
        response = test_client.put(
            '/api/v1/showtime/1', data=data, headers=auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'showtimes': [
                         {'id': 1, 'show_date_time':
                          '2019-10-10 00:00:00',
                          'movie': 'sim',
                          'price': 20000,
                          'cinemahall': 'Cinema1',
                          'available_seats': None}]})
