from datetime import datetime

from flask import request
from flask_restplus import Resource
from webargs import fields as flds  # noqa

from apps.cinema import api
from apps.cinema.schema import validate_date
from apps.cinema.schema.parser import use_args
from apps.cinema.schema.showtime_schema import *
from apps.middlewares.auth import is_admin, token_header
from controllers.show_time_controller import ShowTimeController
from apps.cinema.schema import param

showtime_args = {
    "start_date": param(flds.Str(required=True,validate=validate_date)),
    'id': param(flds.Int(required=True))
}


@api.route('/showtime', endpoint='showtimes')
class ShowTimeEndpoint(Resource):
    @api.marshal_with(showtimes_schema, envelope='showtimes', skip_none=True)
    @token_header
    @use_args(showtime_args)
    def get(self, params):
        showtimes = ShowTimeController()
        params = {items.get('field'): items.get('value') for items in params}
        return showtimes.find(**params), 200

    @api.marshal_with(showtimes_schema, envelope='showtimes', skip_none=True)
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        api.schema_model('ShowTime', {**schema}).validate(body)
        showtimes = ShowTimeController()
        return showtimes.insert(body), 201


@api.route('/showtime/<int:showtime_id>', endpoint='showtime')
class ShowTimeEndpoint(Resource):
    @api.marshal_with(showtimes_schema, envelope='showtime', skip_none=True)
    @token_header
    def get(self, showtime_id, **kwargs):
        showtimes = ShowTimeController()
        return showtimes.find(id=showtime_id, start_date=datetime(2018, 1, 1)), 200

    @api.marshal_with(showtimes_schema, envelope='showtimes', skip_none=True)
    @token_header
    @is_admin
    def put(self, showtime_id):
        body = api.payload
        api.schema_model('ShowTime', {**schema}).validate(body)
        showtimes = ShowTimeController()
        return showtimes.update(id=showtime_id, record=body, serialize=True), 200
