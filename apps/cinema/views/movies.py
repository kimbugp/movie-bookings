from flask import request

from apps.cinema import api
from apps.cinema.schema import validate_json
from apps.cinema.schema.movie_schema import *
from apps.middlewares.auth import is_admin, token_header
from controllers.movies_controller import MovieController
from flask_restplus import Model, Resource, fields, marshal_with

movie_response_schema = api.schema_model('Movie', {**schema})


@api.route('/movie', endpoint='movies')
class MoviesResource(Resource):
    # @marshal_with(movie_response_schema, envelope='movie')
    @api.response(200, "OK", movie_response_schema)
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        movie_response_schema.validate(body)
        # validate_json(body, schema)
        controller = MovieController()
        return controller.insert(body), 201

    @token_header
    @is_admin
    def get(self):
        controller = MovieController()
        return controller.find(), 200


@api.route('/movie/<int:movie_id>', endpoint='movie')
class SingleMovieResource(Resource):
    @token_header
    @is_admin
    def get(self, movie_id):
        controller = MovieController()
        return controller.find(id=movie_id), 200
