from flask import Blueprint, jsonify, request

from apps.cinema import api
from apps.cinema.schema.ticket_schema import *
from apps.middlewares.auth import token_header
from controllers.ticket_controller import TicketController
from flask_restplus import Resource


@api.route('/tickets', endpoint='tickets')
class TicketBookings(Resource):
    @api.marshal_with(ticket_response_body, envelope='ticket')
    @api.expect(ticket_schema)
    @token_header
    def post(self):
        body = api.payload or {}
        validate_json(body, schema)
        body['user_id'] = request.user.get('id')
        controller = TicketController()        
        ticket = controller.insert(**body)
        return ticket

    # @api.marshal_with(user_schema_fields, envelope='user')
    # @api.doc(security='Authorisation')
    # def get(self):
    #     return request.user, 200
