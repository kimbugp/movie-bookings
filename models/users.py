from .base_model import Model as db


class Users(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    email = db.fields(db.string(100), db.not_null())
    password = db.fields(db.string(100), db.unique(), db.not_null())
    name = db.fields(db.date(), db.not_null(False))
