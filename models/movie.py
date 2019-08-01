from database import Model as db


class Movie(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    name = db.fields(db.string(100), db.not_null())
    category = db.fields(db.string(100), db.not_null())
    date_of_release = db.fields(db.date(), db.not_null())
    rating = db.fields(db.integer(), db.not_null())


class ShowTime(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    date = db.fields(db.date(), db.not_null())
    movie_id = db.fields(db.integer(), db.not_null(), db.foreignkey(
        'movie.id', on_delete_cascade=True))
    price = db.fields(db.numeric(), db.not_null())
    cinema_hall = db.fields(db.serial(), db.unique(), db.not_null(True))


class Seat(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    number = db.fields(db.string(100), db.not_null(), db.unique())
