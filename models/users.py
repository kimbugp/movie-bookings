from database import Model as db


class Users(db):
    id = db.fields(db.serial(), db.primary())
    date_created = db.fields(db.datetime(auto_add=True))
    email = db.fields(db.string(100), db.unique(), db.not_null(True))
    password = db.fields(db.string(100), db.not_null(True))
    name = db.fields(db.string(100), db.not_null(False))
    is_staff = db.fields(db.boolean(default=False), db.not_null())
