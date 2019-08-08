from apps.cinema import api
from apps.cinema.schema.showtime_schema import *
from apps.middlewares.auth import token_header, is_admin
from controllers.show_time_controller import ShowTimeController
from flask_restplus import Resource
from flask import request
from apps.cinema.schema import validate_json


@api.route('/showtime', endpoint='showtimes')
class ShowTimeEndpoint(Resource):
    @api.marshal_with(showtimes_schema, envelope='showtimes')
    @token_header
    def get(self):
        showtimes = ShowTimeController()
        return showtimes.findall(), 200

    @api.marshal_with(showtimes_schema, envelope='showtimes')
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        validate_json(body, schema)
        showtimes = ShowTimeController()
        return showtimes.create(**body), 201


@api.route('/showtime/<int:showtime_id>', endpoint='showtime')
class ShowTimeEndpoint(Resource):
    @api.marshal_with(showtimes_schema, envelope='showtime')
    @token_header
    def get(self, showtime_id):
        showtimes = ShowTimeController()
        return showtimes.find(showtime_id), 200

    @api.marshal_with(showtimes_schema, envelope='showtimes')
    @token_header
    @is_admin
    def put(self, showtime_id):
        body = api.payload
        validate_json(body, schema)
        showtimes = ShowTimeController()
        return showtimes.update(id=showtime_id, **body), 200
