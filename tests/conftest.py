from flask import jsonify, make_response, current_app
import pytest
from main import create_app
from utils import NotFound, create_tables, seed_data
import json


def raise_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@pytest.yield_fixture(scope='session')
def app_and_db():
    app, db = create_app('testing')
    app.testing = True
    app.register_error_handler(NotFound, raise_not_found)
    app_context = app.app_context()
    app_context.push()

    yield app, db

    app_context.pop()


@pytest.fixture(scope='class')
def test_client(app_and_db, init_db):
    app, db = app_and_db
    yield app.test_client()


@pytest.fixture(scope='module')
def init_db(app_and_db):
    app, db = app_and_db
    seed_data(db)
    yield db
    db.drop_all()


@pytest.fixture(scope="function")
def base_test_case(request, test_client, init_db):
    request.cls.test_client = test_client
    request.cls.db = init_db


@pytest.fixture(scope='function')
def auth_header(get_token):
    return {'Content-Type': 'application/json',
            'Authorization': get_token}


@pytest.fixture(scope='function')
def registration(test_client):
    data = json.dumps({
        "email": "string@bb.com",
        "name": "string",
        "password": "dsfdsf",
        "is_staff": True
    })
    response = test_client.post(
        '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
    return response


@pytest.fixture(scope='function')
def get_token(test_client, registration):
    response = test_client.post(
        '/api/v1/login', data=json.dumps({
            "email": "string@bb.com",
            "password": "dsfdsf"
        }), headers={'Content-Type': 'application/json'})
    return response.json.get('user').get('token')


@pytest.fixture(scope='function')
def get_admin_token(test_client, registration):
    response = test_client.post(
        '/api/v1/login', data=json.dumps({
            "email": "string@bb.com",
            "password": "dsfdsf"
        }), headers={'Content-Type': 'application/json'})
    return response.json.get('user').get('token')


@pytest.fixture(scope='function')
def showtime(test_client, auth_header):
    data = json.dumps({
        "show_date_time": "2019-11-09 24:00:00",
        "movie_id": 1,
        "price": 20000,
        "cinema_hall": 1
    })
    response = test_client.post(
        '/api/v1/showtime', data=data, headers=auth_header)
    return response, data


@pytest.fixture(scope='function')
def cinema(test_client, auth_header):
    data = json.dumps({
        "name": "CInema25",
        "description": "sdfgd",
        "seats": ["A13", "B34", "w23"]
    })
    response = test_client.post(
        '/api/v1/cinema', data=data, headers=auth_header)
    return response, data
