from database import Model as db


class Ticket(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    payment_method = db.fields(db.string(10), db.not_null())
    user_id = db.fields(db.integer(), db.not_null(),
                        db.foreignkey('users.id', on_delete_cascade=True))
    showtime_id = db.fields(db.integer(), db.not_null(), db.foreignkey(
        'showtime.id', on_delete_cascade=True))
    seat_number = db.fields(db.string(100), db.not_null(), db.foreignkey(
        'seat.seat_number', on_delete_cascade=True))

    class _Meta_:
        unique_together = ('showtime_id', 'seat_number')
