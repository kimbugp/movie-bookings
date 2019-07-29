from .base_model import Model as db


class Ticket(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    payment_method = db.fields(db.text(), db.not_null())
    user_id = db.fields(db.integer(), db.not_null(),
                        db.foreignkey('users.id', on_delete_cascade=True))
    showtime_id = db.fields(db.integer(), db.not_null(), db.foreignkey(
        'showtime.id', on_delete_cascade=True))
    seat = db.fields(db.string(100), db.not_null(), db.foreignkey(
        'seat.number', on_delete_cascade=True))
