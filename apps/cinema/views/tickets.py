from flask import request
from flask_restplus import Resource
from webargs import fields as flds

from apps.cinema import api
from apps.cinema.schema import param, validate_date
from apps.cinema.schema.parser import use_args
from apps.cinema.schema.ticket_schema import (
    process_tickets_seats,
    schema,
    ticket_response_body,
    ticket_schema,
)
from apps.middlewares.auth import token_header
from controllers.ticket_controller import TicketController

ticket_args = {
    "user_id": param(flds.Int(required=True)),
    "date_created": param(flds.Str(validate=validate_date)),
    "show_datetime": param(flds.Str(validate=validate_date)),
    "movie_id": param(flds.Int()),
    "price": param(flds.Float()),
    "id": param(flds.Int()),
}


@api.route("/ticket", endpoint="tickets")
class TicketBookings(Resource):
    @api.marshal_with(ticket_response_body, envelope="ticket", skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    def post(self):
        body = api.payload or {}
        api.schema_model("Tickets", {**schema}).validate(body)
        body["user_id"] = request.user.id
        controller = TicketController()

        seats_ids = body.pop("seat_id")
        seat_list = seats_ids if type(seats_ids) is list else [seats_ids]

        seats = process_tickets_seats(body, seat_list)
        ticket = controller.insert(seats, seat_id=seat_list, **body)

        return ticket, 201

    @api.marshal_with(ticket_response_body, envelope="tickets", skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    @use_args(ticket_args)
    def get(self, params, **kwargs):
        user_id = request.user.id
        controller = TicketController()
        if not request.user.is_staff:
            params.append(
                {"operator": "=", "value": user_id, "field": "user_id"}
            )
        tickets = controller.find(
            serialize=True, operator="AND", params=params, **kwargs
        )
        return tickets, 200


@api.route("/ticket/<int:ticket_id>", endpoint="ticket")
class TicketBooking(Resource):
    @api.marshal_with(ticket_response_body, envelope="ticket", skip_none=True)
    @api.expect(ticket_schema)
    @token_header
    def get(self, ticket_id, **kwargs):
        user_id = request.user.id
        controller = TicketController()
        ticket = controller.find_one(
            user_id=user_id, id=ticket_id, serialize=True
        )
        return ticket
