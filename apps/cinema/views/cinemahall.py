from flask import request

from apps.cinema import api
from apps.cinema.schema import validate_json
from apps.cinema.schema.cinema_schema import *
from apps.middlewares.auth import is_admin, token_header
from controllers.cinema import CinemaController
from controllers.seats import SeatController
from flask_restplus import Resource
from utils import dict_to_tuple


@api.route('/cinema', endpoint='cinema')
class CinemaEndpoint(Resource):
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        api.schema_model('cinema', {**schema}).validate(body)
        seats = body.pop('seats')
        controller = CinemaController()
        cinema = controller.insert(body)
        seats_dict = process_seats(seats)
        SeatController().insert(seats_dict)
        return {'seats': seats, **cinema}, 201


def process_seats(seats):
    results = []
    for col in seats:
        numbers = col.get('number')
        [results.append({'cinema_hall': 1, 'number': item,
                        'name': col.get('name'), }) for item in numbers]
        
    return results
