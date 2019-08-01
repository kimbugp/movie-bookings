from flask import Blueprint, jsonify, request

from apps.cinema import api
from controllers.user_controller import UserController
from flask_restplus import Resource
from apps.cinema.schema.user_schema import user_schema


@api.route('/auth')
class UserRegistration(Resource):
    @api.marshal_with(user_schema, envelope='users')
    def post(self):
        user = api.payload
        controller = UserController()
        user = controller.insert(**user)
        return jsonify(**user), 201
