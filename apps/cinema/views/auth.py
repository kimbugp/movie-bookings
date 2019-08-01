from flask import Blueprint, jsonify, request

from apps.cinema import api
from apps.cinema.schema.user_schema import (user_request_fields,
                                            user_schema_fields)
from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController
from flask_restplus import Resource


@api.route('/auth', endpoint='users')
class UserRegistration(Resource):
    @api.marshal_with(user_schema_fields, envelope='user')
    @api.expect(user_request_fields)
    def post(self):
        user = api.payload
        controller = UserController()
        if not controller.find(email=user.get('email')):
            user = controller.insert(**user)
            return user, 201
        raise ValidationError(message='error', status_code=400, payload={
                              'message': 'User with email already exists'})
