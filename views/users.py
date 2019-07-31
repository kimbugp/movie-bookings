from flask import Blueprint, jsonify, request

from controllers.user_controller import UserController

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('', methods=['POST'])
def create():
    user = request.get_json()
    controller = UserController()
    user = controller.insert(**user)
    return jsonify(**user), 201
