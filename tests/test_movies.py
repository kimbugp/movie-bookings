import json

import psycopg2

from .basetest import BaseTestCase


class TestMovies(BaseTestCase):
    def test_create_movie_fails_with_no_authentication(self, test_client):
        data = json.dumps({})
        response = test_client.post(
            "/api/v1/movie",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 401

    def test_create_cinema_with_no_permissions_fails(self, test_client):
        response = test_client.post("/api/v1/movie")
        assert response.status_code == 401

    def test_create_movie_succeeds(self, movie):
        response, data = movie
        self.assertEqual(
            response.json,
            {
                "movie": [
                    {
                        "id": 3,
                        "name": "Lord of thmke rings",
                        "date_of_release": "2019-11-09 00:00:00",
                        "length": "02:30:00",
                        "summary": "Simoejnjlkanfwdybusnrj,",
                        "category": "somejr",
                        "rating": 1,
                    }
                ]
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_get_all_movies(self, test_client, movie, auth_header):
        response = test_client.get("/api/v1/movie", headers=auth_header)
        self.assertEqual(response.status_code, 200)

    def test_get_movie_by_id(self, test_client, movie, auth_header):
        response = test_client.get("/api/v1/movie/1", headers=auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                "movie": {
                    "id": 1,
                    "name": "sim",
                    "date_of_release": "2019-08-05 00:00:00",
                    "length": "02:30:00",
                    "summary": "sdfsdfdgdsd",
                    "category": "horror",
                    "rating": 1,
                }
            },
        )

    def test_update_movie_by_id_succeeds(
        self, test_client, movie, auth_header
    ):
        _, data = movie
        response = test_client.put(
            "/api/v1/movie/1", data=data, headers=auth_header
        )
        self.assertEqual(
            response.json["movie"][0],
            {
                "id": 1,
                "name": "Lord of thmke rings",
                "date_of_release": "2019-11-09 00:00:00",
                "length": "02:30:00",
                "summary": "Simoejnjlkanfwdybusnrj,",
                "category": "somejr",
                "rating": 1,
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_update_show_time_by_id_fails(
        self, test_client, movie, auth_header
    ):
        _, data = movie
        response = test_client.put(
            "/api/v1/movie/100", data=data, headers=auth_header
        )
        self.assertEqual(response.status_code, 404)
