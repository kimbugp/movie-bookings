import datetime
from functools import wraps

import jwt
from flask import current_app, jsonify, make_response, request

from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController


def token_header(f):
    ''' Function to get the token using the header'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            raise ValidationError(message='error', status_code=401, payload={
                'message': 'No auth token'})
        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
            controller = UserController()
            user = controller.find_one(email=data.get('email'))
            request.user = user
        except Exception as error:
            raise ValidationError(message='error', status_code=401, payload={
                'message': 'Invalid token'})
        return f(*args, **kwargs)
    return decorated


def generate_token(user):
    user.pop('password')
    token = jwt.encode({
        'exp': datetime.datetime.utcnow() +
        datetime.timedelta(minutes=60), **user},
        current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
