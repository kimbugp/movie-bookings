from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from apps.cinema import api
from apps.cinema.schema.user_schema import *
from apps.middlewares.auth import generate_token, is_admin, token_header
from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController
from flask_restplus import Resource
from webargs import fields as flds
from webargs.flaskparser import use_args
from apps.cinema.schema import validate_date


user_args = {'id': flds.Int(),
             'email': flds.Str(),
             'report': flds.Bool(),
             'name': flds.Str(),
             'ticket_startdate': flds.Str(validate=validate_date),
             'ticket_enddate': flds.Str(validate=validate_date),
             'total': flds.Float()}


@api.route('/auth', endpoint='user')
class UserRegistration(Resource):
    @api.marshal_with(user_schema_fields, envelope='user', skip_none=True)
    @api.expect(user_request_fields)
    def post(self):
        user = api.payload
        api.schema_model('User', {**user_schema}).validate(user)
        user['password'] = generate_password_hash(
            user['password'], method='sha256')
        controller = UserController()
        if not controller.find(email=user.get('email')):
            user = controller.insert(user)
            return user, 201
        raise ValidationError(message='error', status_code=400, payload={
                              'message': 'User with email already exists'})

    @api.marshal_with(user_schema_fields, envelope='user', skip_none=True)
    @api.doc(security='Authorisation')
    @token_header
    def get(self):
        return request.user._asdict(), 200


@api.route('/login', endpoint='login')
class LoginResource(Resource):
    @api.marshal_with(login_schema, envelope='user', skip_none=True)
    @api.expect(user_request_fields)
    def post(self):
        request_data = api.payload
        api.schema_model(
            'User', {**user_login_schema}).validate(request_data)
        controller = UserController()
        user = controller.find_one(email=request_data.get('email'))
        if user and check_password_hash(user.password, request_data['password']):
            token = generate_token(user)
            return {'token': token, **user._asdict()}, 200
        raise ValidationError(message='error', status_code=401, payload={
                              'message': 'Invalid credentials'})


@api.route('/users', endpoint='users')
class UserQueryAndReport(Resource):

    @api.marshal_with(user_schema_fields, envelope='user', skip_none=True)
    @token_header
    @is_admin
    @use_args(user_args)
    def get(self, args):
        controller = UserController()
        return controller.find(serialize=True, **args), 200
