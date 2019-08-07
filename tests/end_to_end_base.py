import json

from .basetest import BaseTestCase


class EndToEndBase(BaseTestCase):

    def get_token(self):
        data = json.dumps({
            "email": "string@bb.com",
            "name": "string",
            "password": "dsfdsf",

        })
        self.test_client.post(
            '/api/v1/auth', data=data, headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/api/v1/login', data=data, headers={'Content-Type': 'application/json'})
        return response.json.get('user').get('token')
