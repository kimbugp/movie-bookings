from flask import current_app, request

from apps.cinema import api
from apps.cinema.schema.cinema_schema import *
from apps.middlewares.auth import is_admin, token_header
from controllers.cinema import CinemaController
from controllers.seats import SeatController
from flask_restplus import Resource
from models import CinemaHall
from utils import dict_to_tuple, find_or_404


@api.route('/cinema', endpoint='cinemas')
class CinemasEndpoint(Resource):
    @api.marshal_with(cinema_response_schema, envelope='cinema', skip_none=True)
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        api.schema_model('cinema', {**schema}).validate(body)
        seats = body.pop('seats')
        controller = CinemaController()
        cinema = controller.insert(body)[0]
        seats_dict = process_seats(seats, cinema.get('id'))
        SeatController().insert(seats_dict)
        return {'seats': SeatController().insert(seats_dict), **cinema}, 201


@api.route('/cinema/<int:cinema_id>', endpoint='cinema')
class CinemaEndpoint(Resource):
    @api.marshal_with(cinema_response_schema, envelope='cinema', skip_none=True)
    @token_header
    @token_header
    @is_admin
    def put(self, cinema_id):
        body = api.payload
        schema['required'] = ["seats"]
        api.schema_model('cinema', {**schema}).validate(body)
        seats = body.pop('seats')
        controller = CinemaController()
        cinema = find_or_404(current_app.db, CinemaHall, id=cinema_id)
        seats_dict = SeatController().insert(process_seats(seats, cinema.id))
        return {'seats': seats_dict, **cinema._asdict()}, 200
