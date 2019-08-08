from flask import Blueprint, jsonify, request

from apps.cinema import api
from apps.cinema.schema.ticket_schema import *
from apps.middlewares.auth import token_header
from controllers.ticket_controller import TicketController
from flask_restplus import Resource


@api.route('/ticket', endpoint='tickets')
class TicketBookings(Resource):
    @api.marshal_with(ticket_response_body, envelope='ticket')
    @api.expect(ticket_schema)
    @token_header
    def post(self):
        body = api.payload or {}
        validate_json(body, schema)
        body['user_id'] = request.user.id
        controller = TicketController()
        ticket = controller.insert(body)
        return ticket

    @api.marshal_with(ticket_response_body, envelope='tickets')
    @api.expect(ticket_schema)
    @token_header
    def get(self):
        user_id = request.user.id
        controller = TicketController()
        tickets = controller.find(user_id=user_id, serialize=True)
        return tickets, 200


@api.route('/ticket/<int:ticket_id>', endpoint='ticket')
class TicketBooking(Resource):
    @api.marshal_with(ticket_response_body, envelope='tickets')
    @api.expect(ticket_schema)
    @token_header
    def get(self, ticket_id):
        user_id = request.user.id
        controller = TicketController()
        ticket = controller.find_one(
            operator='AND', user_id=user_id, id=ticket_id, serialize=True)
        return ticket
