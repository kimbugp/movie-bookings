from database import Model as db


class Users(db):
    id = db.fields(db.serial(), db.primary())
    email = db.fields(db.string(100), db.unique(), db.not_null(True))
    password = db.fields(db.string(100), db.not_null(True))
    name = db.fields(db.string(100), db.not_null(False))
