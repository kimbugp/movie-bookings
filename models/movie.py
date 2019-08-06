from database import Model as db


class Movie(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    name = db.fields(db.string(100), db.not_null(True))
    category = db.fields(db.string(100), db.not_null(True))
    date_of_release = db.fields(db.datetime(), db.not_null())
    rating = db.fields(db.integer(), db.not_null())


class ShowTime(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    show_date_time = db.fields(db.datetime(), db.not_null())
    movie_id = db.fields(db.integer(), db.not_null(), db.foreignkey(
        'movie.id', on_delete_cascade=True))
    price = db.fields(db.numeric(), db.not_null())
    cinema_hall = db.fields(db.integer(), db.foreignkey(
        'cinemahall.id', on_delete_cascade=True))


class Seat(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    seat_number = db.fields(db.string(100), db.not_null(), db.unique())
    cinema_hall = db.fields(db.integer(), db.foreignkey(
        'cinemahall.id', on_delete_cascade=True))


class CinemaHall(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    name = db.fields(db.string(100), db.not_null(), db.unique())
    description = db.fields(db.string(100), db.not_null())
