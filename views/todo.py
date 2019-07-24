from flask import Blueprint, request, jsonify
from controllers.todo_controller import TodoController


todo = Blueprint('todo', __name__, url_prefix='/todo')


@todo.route('', methods=['POST'])
def create():
    todo = request.json
    controller = TodoController(todo)
    new_todo = controller.save()
    return jsonify(**todo), 201


@todo.route('/<string:id>', methods=['GET'])
def get(id):
    controller = TodoController()
    todo = controller.get(id)
    return todo


@todo.route('/<string:id>', methods=['DELETE'])
def delete(id):
    controller = TodoController()
    todo = controller.delete(id)
    return jsonify(message='Item has been deleted'), 200


@todo.route('/<string:id>', methods=['PUT'])
def update(id):
    todo = request.json
    controller = TodoController()
    todo = controller.update(id, todo)
    return jsonify(**todo), 200
