from flask import Blueprint, jsonify, request

from controllers.ticket_controller import TicketController

ticket = Blueprint('ticket', __name__, url_prefix='/ticket')


@ticket.route('', methods=['POST'])
def create():
    """Create a ticket

    Args:
        showtime_id (int): movie show time
        seat(string): movie theatre street
        payment_method(): payment method
    """
    ticket = request.get_json()
    controller = TicketController(ticket)
    new_ticket = controller.save()
    return jsonify(**ticket), 201
