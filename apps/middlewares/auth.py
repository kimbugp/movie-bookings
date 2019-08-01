import datetime
from functools import wraps

import jwt
from flask import current_app, jsonify, make_response, request


def token_header(f):
    ''' Function to get the token using the header'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorisation', None)
        if not token:
            return make_response(jsonify({'message': 'No auth token'}), 401)
        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
            user_id = 1
        except:
            return make_response(jsonify({'message': 'Invalid token'}), 401)
        return f(user_id, *args, **kwargs)
    return decorated


def generate_token(user):
    user.pop('password')
    token = jwt.encode({
        'exp': datetime.datetime.utcnow() +
        datetime.timedelta(minutes=60), **user},
        current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
