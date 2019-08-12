from flask import Blueprint, jsonify, request

from apps.cinema import api
from apps.cinema.schema.ticket_schema import *
from apps.cinema.schema import validate_date
from apps.middlewares.auth import token_header
from controllers.ticket_controller import TicketController
from flask_restplus import Resource
from webargs import fields
from webargs.flaskparser import use_args

ticket_args = {'user_id': fields.Int(),
               'date_created': fields.Str(validate=validate_date),
               'show_date_time': fields.Str(validate=validate_date),
               'movie_id': fields.Int(),
               'price': fields.Float(),
               'id': fields.Int()}


@api.route('/ticket', endpoint='tickets')
class TicketBookings(Resource):
    @api.marshal_with(ticket_response_body, envelope='ticket', skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    def post(self):
        body = api.payload or {}
        api.schema_model('Tickets', {**schema}).validate(body)
        body['user_id'] = request.user.id
        controller = TicketController()

        seats_ids = body.pop('seat_id')
        seat_list = seats_ids if type(seats_ids) is list else [seats_ids]

        seats = process_tickets_seats(body, seat_list)
        ticket = controller.insert(seats, seat_id=seat_list, **body)

        return ticket, 201

    @api.marshal_with(ticket_response_body, envelope='tickets', skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    @use_args(ticket_args)
    def get(self, args):
        user_id = request.user.id
        controller = TicketController()
        if not request.user.is_staff:
            args['user_id'] = request.user.id
        tickets = controller.find(
            serialize=True, operator='AND', **args)
        return tickets, 200


@api.route('/ticket/<int:ticket_id>', endpoint='ticket')
class TicketBooking(Resource):
    @api.marshal_with(ticket_response_body, envelope='ticket', skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    def get(self, ticket_id):
        user_id = request.user.id
        controller = TicketController()
        ticket = controller.find_one(
            operator='AND', user_id=user_id, id=ticket_id, serialize=True)
        return ticket
