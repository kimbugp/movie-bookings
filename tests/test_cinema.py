import json

import psycopg2

from .basetest import BaseTestCase


class TestCinema(BaseTestCase):
    def test_create_cinema_fails_with_no_authentication(self, test_client):
        data = json.dumps({})
        response = test_client.post(
            "/api/v1/cinema",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 401)

    def test_create_cinema_with_no_permissions_fails(self, test_client):
        response = test_client.post("/api/v1/cinema")
        self.assertEqual(response.status_code, 401)

    def test_get_cinema(self, test_client, auth_header):
        response = test_client.get("/api/v1/cinema", headers=auth_header)
        self.assertEqual(response.status_code, 200)

    def test_create_show_time_fails_with_cinema_hall_already_filled(
        self, test_client, auth_header, cinema
    ):
        _, data = cinema
        response = test_client.post(
            "/api/v1/cinema", data=data, headers=auth_header
        )
        assert response.status_code == 400

    def create_cinema_succeeds(self, cinema):
        response, data = cinema
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json,
            {
                "seats": [
                    {"name": "A", "number": [1, 2]},
                    {"name": "B", "number": [1, 2]},
                ],
                "id": 4,
                "name": "Simon Peter",
                "description": "sdfgd",
            },
        )


class TestUpdateCinema(BaseTestCase):
    def test_update_cinema_by_id_succeeds(
        self, test_client, cinema, auth_header
    ):
        data = json.dumps(
            {
                "seats": [
                    {"name": "C", "number": [1, 2]},
                    {"name": "D", "number": [1, 2]},
                ]
            }
        )
        response = test_client.put(
            "/api/v1/cinema/1", data=data, headers=auth_header
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                "cinema": {
                    "id": 1,
                    "name": "Cinema1",
                    "description": "SOme data",
                    "seats": [
                        {
                            "id": 12,
                            "name": "C",
                            "number": "1",
                            "cinema_hall": 1,
                        },
                        {
                            "id": 13,
                            "name": "C",
                            "number": "2",
                            "cinema_hall": 1,
                        },
                        {
                            "id": 14,
                            "name": "D",
                            "number": "1",
                            "cinema_hall": 1,
                        },
                        {
                            "id": 15,
                            "name": "D",
                            "number": "2",
                            "cinema_hall": 1,
                        },
                    ],
                }
            },
        )

    def test_update_cinema_by_id_fails(self, test_client, cinema, auth_header):
        _, data = cinema
        response = test_client.put(
            "/api/v1/cinema/100", data=data, headers=auth_header
        )
        self.assertEqual(response.status_code, 404)

    def test_update_cinema_by_id_fails_wth_same_seats(
        self, test_client, auth_header
    ):
        data = json.dumps(
            {
                "seats": [
                    {"name": "A", "number": [1, 2]},
                    {"name": "B", "number": [1, 2]},
                ]
            }
        )
        response = test_client.put(
            "/api/v1/cinema/4", data=data, headers=auth_header
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json,
            {
                "error": "  Key (name, cinema_hall, number)=(A, 4, 1) already exists.\n",
                "message": "",
            },
        )
