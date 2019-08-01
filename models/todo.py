from database import Model as db


class Todo(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    description = db.fields(db.text(), db.not_null())
    slug = db.fields(db.string(100), db.unique(), db.not_null())
    name = db.fields(db.date(), db.not_null(False))
    users_id = db.fields(db.integer(), db.not_null(
        False), db.foreignkey('users.id', on_delete_cascade=True))
