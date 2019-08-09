from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from apps.cinema import api
from apps.cinema.schema.user_schema import *
from apps.middlewares.auth import generate_token, token_header
from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController
from flask_restplus import Resource


@api.route('/auth', endpoint='users')
class UserRegistration(Resource):
    @api.marshal_with(user_schema_fields, envelope='user')
    @api.expect(user_request_fields)
    def post(self):
        user = api.payload
        validate_json(user, user_schema)
        user['password'] = generate_password_hash(
            user['password'], method='sha256')
        controller = UserController()
        if not controller.find(email=user.get('email')):
            user = controller.insert(user)
            return user, 201
        raise ValidationError(message='error', status_code=400, payload={
                              'message': 'User with email already exists'})

    @api.marshal_with(user_schema_fields, envelope='user')
    @api.doc(security='Authorisation')
    @token_header
    def get(self):
        return request.user._asdict(), 200


@api.route('/login', endpoint='login')
class LoginResource(Resource):
    @api.marshal_with(login_schema, envelope='user')
    @api.expect(user_request_fields)
    def post(self):
        request_data = api.payload
        validate_json(request_data, user_login_schema)
        controller = UserController()
        user = controller.find_one(email=request_data.get('email'))
        if user and check_password_hash(user.password, request_data['password']):
            token = generate_token(user._asdict())
            return {'token': token, **user._asdict()}, 200
        raise ValidationError(message='error', status_code=401, payload={
                              'message': 'Invalid credentials'})
