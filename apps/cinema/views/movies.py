import datetime

from flask import jsonify, request

from apps.cinema import api
from apps.cinema.schema.movie_schema import *
from apps.middlewares.auth import is_admin, token_header
from controllers.movies_controller import MovieController
from flask_restplus import Model, Resource, fields, marshal_with


@api.route('/movie', endpoint='movies')
class MoviesResource(Resource):
    @api.marshal_with(movie_response_schema, envelope='movie', skip_none=True)
    @token_header
    @is_admin
    def post(self):
        body = api.payload
        api.schema_model('Movie', {**schema}).validate(body)
        controller = MovieController()
        movie = controller.insert(body)
        return movie, 201

    @api.marshal_with(movie_response_schema, envelope='movies', skip_none=True)
    @token_header
    @is_admin
    def get(self):
        controller = MovieController()
        return controller.find(serialize=True), 200


@api.route('/movie/<int:movie_id>', endpoint='movie')
class SingleMovieResource(Resource):
    @api.marshal_with(movie_response_schema, envelope='movie', skip_none=True)
    @token_header
    def get(self, movie_id):
        controller = MovieController()
        return controller.find(id=movie_id, serialize=True), 200

    @api.marshal_with(movie_response_schema, envelope='movie', skip_none=True)
    @token_header
    @is_admin
    def put(self, movie_id):
        body = api.payload
        api.schema_model('movie', {**schema}).validate(body)
        controller = MovieController()
        return controller.update(id=movie_id, record=body, serialize=True), 200
