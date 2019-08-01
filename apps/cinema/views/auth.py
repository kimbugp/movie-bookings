from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from apps.cinema import api
from apps.cinema.schema.user_schema import *
from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController
from flask_restplus import Resource
from apps.middlewares.auth import generate_token


@api.route('/register', endpoint='users')
class UserRegistration(Resource):
    @api.marshal_with(user_schema_fields, envelope='user')
    @api.expect(user_request_fields)
    def post(self):
        user = api.payload
        process_user_json(user)
        user['password'] = generate_password_hash(
            user['password'], method='sha256')
        controller = UserController()
        if not controller.find(email=user.get('email')):
            user = controller.insert(**user)
            return user, 201
        raise ValidationError(message='error', status_code=400, payload={
                              'message': 'User with email already exists'})


@api.route('/login', endpoint='login')
class LoginResource(Resource):
    @api.marshal_with(login_schema, envelope='user')
    @api.expect(user_request_fields)
    def post(self):
        request_data = api.payload
        process_signin_json(request_data)
        controller = UserController()
        user = controller.find_one(email=request_data.get('email'))
        if user and check_password_hash(user.get('password'), request_data['password']):
            user['token'] = str(generate_token(user))
            return user, 200
        raise ValidationError(message='error', status_code=401, payload={
                              'message': 'Invalid credentials'})
