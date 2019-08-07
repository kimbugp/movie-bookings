from flask import jsonify, make_response, current_app
import pytest
from main import create_app
from utils import NotFound, create_tables


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
def test_client(app_and_db):
    app, db = app_and_db
    yield app.test_client()


@pytest.fixture(scope='module')
def init_db(app_and_db):
    app, db = app_and_db
    create_tables(db)
    yield db
    db.drop_all()


@pytest.fixture(scope="class")
def base_test_case(request, test_client, init_db):
    request.cls.test_client = test_client
    request.cls.db = init_db
