from database import Model as db
from sql import get_cte_query


class Movie(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    date_created = db.fields(db.datetime(auto_add=True))

    name = db.fields(db.string(100), db.not_null(True))
    category = db.fields(db.string(100), db.not_null(True))
    date_of_release = db.fields(db.datetime(), db.not_null())
    rating = db.fields(db.integer(), db.not_null())
    length = db.fields(db.time(), db.not_null())
    summary = db.fields(db.text(), db.not_null(False))


class ShowTime(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    date_created = db.fields(db.datetime(auto_add=True))

    show_date_time = db.fields(db.datetime(), db.not_null())
    movie_id = db.fields(db.integer(), db.not_null(), db.foreignkey(
        'movie.id', on_delete_cascade=True))
    price = db.fields(db.numeric(), db.not_null())
    cinema_hall = db.fields(db.integer(), db.foreignkey(
        'cinemahall.id', on_delete_cascade=True))

    class _Meta_:
        unique_together = ('show_date_time', 'movie_id')

    def insert_query(self, records):
        query = super().insert_query(records)
        return get_cte_query('showtime_insert').format(query)

    def clean(self, query):
        return get_cte_query('clean_showtime').format(**query)

    def update(self, id, operator, **kwargs):
        query = super().update(id, operator, **kwargs)
        return get_cte_query('showtime_insert').format(query)


class Seat(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    name = db.fields(db.string(100), db.not_null())
    number = db.fields(db.integer(), db.not_null())
    date_created = db.fields(db.datetime(auto_add=True))
    cinema_hall = db.fields(db.integer(), db.foreignkey(
        'cinemahall.id', on_delete_cascade=True))

    class _Meta_:
        unique_together = ('name', 'cinema_hall', 'number')


class CinemaHall(db):
    id = db.fields(db.serial(), db.primary(), db.unique())
    date_created = db.fields(db.datetime(auto_add=True))

    name = db.fields(db.string(100), db.not_null(), db.unique())
    description = db.fields(db.string(100), db.not_null())
