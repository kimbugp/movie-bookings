import datetime
from functools import wraps

import jwt
from flask import current_app, jsonify, make_response, request

from apps.middlewares.validation import ValidationError
from controllers.user_controller import UserController


def token_header(f):
    ''' Function to get  and check the jwt token'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            raise ValidationError(message='error', status_code=401, payload={
                'message': 'No auth token'})
        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            controller = UserController()
            user = controller.find_one(email=data.get('email'))
            if not user:
                raise ValidationError(message='error', status_code=401, payload={
                    'message': 'Invalid token'})
            request.user = user
        except Exception as error:
            raise ValidationError(message='error', status_code=401, payload={
                'message': 'Invalid token'})
        return f(*args, **kwargs)
    return decorated


def generate_token(user):
    token = jwt.encode({
        'exp': datetime.datetime.utcnow() +
        datetime.timedelta(days=60), "email": user.email, "id": user.id, "name": user.name},
        current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    return token


def is_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.user.is_staff:
            raise ValidationError(message='error', status_code=401, payload={
                'message': 'You have not permission to perform this action'})
        return f(*args, **kwargs)
    return decorated
