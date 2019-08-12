import os

from flask import jsonify, make_response
from main import create_app
from utils import NotFound, create_tables, seed_data

app, db = create_app(os.environ.get('FLASK_ENV'))


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def migrate():
    create_tables(db)


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def seed_database():
    seed_data(db)


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def test():
    from subprocess import run
    run('pytest')


@app.errorhandler(NotFound)
def raise_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run()
