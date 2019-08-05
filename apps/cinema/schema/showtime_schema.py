
from flask_restplus import fields


ticket_schema = api.model('ShowTime', {
    'payment_method': fields.String(required=True),
    'seat': fields.String(required=True),
    'showtime_id': fields.Integer(required=True),
})

ticket_response_body = ticket_schema.clone('Ticket', {
    'user': fields.String(required=True)
})
showtime = api.model('ShowTime', {
    'id': fields.String(required=True),
    'show_date_time': fields.String(required=True),
    'movie': fields.String(required=True),
    'price': fields.Integer(required=True),
    'cinema_hall': fields.String(required=True),
    'seats': fields.List(fields.String())

})

showtimes_schema = api.model('ShowTimes', {
    'showtimes': fields.List(fields.Nested(showtime)),
    'count': fields.Integer(required=True)
})
