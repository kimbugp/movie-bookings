from datetime import datetime as dt, timedelta as td


def get_date(hours=0):
    return (dt.now() + td(hours=hours)).strftime('%Y-%m-%d %H:%M:%S')


user = [
    {
        "email": "peter@gmail.com",
        "password": "sha256$HwJeg0Ig$24f5e0f26fe2eb7ffa116b681f90e2f8383c4d0802dd48f5259d43885b38a23d",
        "name": "Simon Peter K",
        "is_staff": "true"
    }
]
cinemahall = [

    {
        "name": "Cinema1",
        "description": "SOme data"
    },
    {
        "name": "Cimena2",
        "description": "something esle"
    },
    {
        "name": "Cinema 3",
        "description": "slef"
    }

]

movie = [
    {
        "date_of_release": "2019-08-05 00:00:00",
        "name": "sim",
        "category": "horror",
        "rating": 1,
        "length": "2:30",
        'summary': 'sdfsdfdgdsd'
    },
    {

        "date_of_release": "2019-08-06 00:00:00",
        "name": "lord of rings",
        "category": "times",
        "rating": 5,
        "length": "2:30",
        'summary': 'sdfdsdfghferw'
    }
]

seat = [
    {

        "number": 1,
        "cinema_hall": 1,
        "name": "a"
    },
    {
        "number": 2,
        "cinema_hall": 1,
        "name": "b"
    },
    {
        "number": 3,
        "cinema_hall": 1,
        "name": "c"
    },
    {
        "number": 2,
        "cinema_hall": 1,
        "name": "d"
    },
    {
        "number": 4,
        "cinema_hall": 1,
        "name": "e"
    },
    {
        "number": 1,
        "cinema_hall": 2,
        "name": "f"
    },
    {
        "number": 4,
        "cinema_hall": 2,
        "name": "g"
    }
]
showtime = [
    {
        "cinema_hall": 1,
        "movie_id": 1,
        "show_datetime": get_date(),
        "price": 20000
    },
    {
        "cinema_hall": 1,
        "movie_id": 1,
        "show_datetime": get_date(2),
        "price": 30000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_datetime": get_date(4),
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 1,
        "show_datetime": get_date(6),
        "price": 20000
    },
    {
        "cinema_hall": 3,
        "movie_id": 1,
        "show_datetime": get_date(8),
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_datetime": "2019-08-06 12:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_datetime": "2019-08-04 12:00:00",
        "price": 20000
    }
]

ticket = [
    {
        "payment_method": "mm",
        "seat_id": 1,
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "seat_id": 2,
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "seat_id": 3,
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "seat_id": 4,
        "user_id": 1,
        "showtime_id": 2
    },
    {
        "payment_method": "mm",
        "seat_id": 5,
        "user_id": 1,
        "showtime_id": 4
    },
    {
        "payment_method": "mm",
        "seat_id": 6,
        "user_id": 1,
        "showtime_id": 4
    }
]
