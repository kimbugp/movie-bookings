import json
from unittest import TestCase

import pytest

from apps.middlewares.validation import ValidationError
from sql import get_cte_query


class BaseTestCase():

    def assertEqual(self, arg1, arg2):
        assert arg1 == arg2

    def assertIn(self, obj, item):
        assert item in obj

    def assertKeys(self, obj, item):
        assert item.items() <= obj.items()

    def assertCountEqual(self, obj, count):
        assert len(obj) == count

    def test_file_not_found(self):
        with pytest.raises(ValidationError) as error:
            get_cte_query('invsf')

    def registration(self, test_client, is_staff=True):
        data = json.dumps({
            "email": "string@bb.com",
            "name": "string",
            "password": "dsfdsf",
            "is_staff": is_staff
        })
        response = test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        return response
