from apps.cinema import api
from apps.cinema.schema.showtime_schema import *
from apps.middlewares.auth import token_header
from controllers.show_time_controller import ShowTimeController
from flask_restplus import Resource
from flask import request


@api.route('/showtime', endpoint='showtime')
class ShowTimeEndpoint(Resource):
    @api.marshal_with(showtimes_schema, envelope='showtime')
    @token_header
    def get(self):
        showtimes = ShowTimeController()
        return showtimes.findall(), 200
