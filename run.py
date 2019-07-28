from main import create_app
import os
from flask import make_response, jsonify

from utils import NotFound


app,db = create_app(os.environ.get('FLASK_ENV'))


@app.errorhandler(NotFound)
def raise_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()
