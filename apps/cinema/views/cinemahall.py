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
        validate_json(body, schema)
        seats = body.pop('seats')
        controller = CinemaController()
        cinema = controller.insert(body)
        seats_dict = [{'cinema_hall': cinema.get(
            'id'), 'seat_number': seat} for seat in seats]
        SeatController().insert(seats_dict)
        return {'seats': seats, **cinema}, 201
