user = [
    {
        "email": "peter@gmail.com",
        "id": 1,
        "password": "sha256$UyheEiSQ$1e5b829d612f4134c0c4848804549652862e795245f5ed1de8c885a81953b3e1",
        "name": "Simon Peter K",
        "is_staff": "true"
    }
]
cinemahall = [

    {
        "id": 1,
        "name": "Cinema1",
        "description": "SOme data"
    },
    {
        "id": 2,
        "name": "Cimena2",
        "description": "something esle"
    },
    {
        "id": 3,
        "name": "Cinema 3",
        "description": "slef"
    }

]

movie = [
    {
        "id": 1,
        "date_of_release": "2019-08-05 00:00:00",
        "name": "sim",
        "category": "horror",
        "rating": 1,
        "length": "2:30"
    },
    {
        "id": 2,
        "date_of_release": "2019-08-06 00:00:00",
        "name": "lord of rings",
        "category": "times",
        "rating": 5,
        "length": "2:30"
    }
]

seat = [
    {
        "id": 1,
        "seat_number": "string",
        "cinema_hall": 1
    },
    {
        "id": 3,
        "seat_number": "h34",
        "cinema_hall": 1
    },
    {
        "id": 4,
        "seat_number": "h56",
        "cinema_hall": 1
    },
    {
        "id": 5,
        "seat_number": "y56",
        "cinema_hall": 1
    },
    {
        "id": 8,
        "seat_number": "d45",
        "cinema_hall": 1
    },
    {
        "id": 2,
        "seat_number": "h23",
        "cinema_hall": 2
    },
    {
        "id": 6,
        "seat_number": "h12",
        "cinema_hall": 2
    },
    {
        "id": 9,
        "seat_number": "e34",
        "cinema_hall": 2
    },
    {
        "id": 7,
        "seat_number": "g34",
        "cinema_hall": 3
    },
    {
        "id": 10,
        "seat_number": "a12",
        "cinema_hall": 3
    },
    {
        "id": 11,
        "seat_number": "e45",
        "cinema_hall": 2
    }
]

showtime = [
    {
        "cinema_hall": 1,
        "id": 1,
        "movie_id": 1,
        "show_date_time": "2019-08-09 08:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 1,
        "id": 2,
        "movie_id": 1,
        "show_date_time": "2019-08-07 00:00:00",
        "price": 30000
    },
    {
        "cinema_hall": 2,
        "id": 3,
        "movie_id": 2,
        "show_date_time": "2019-08-07 00:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "id": 5,
        "movie_id": 1,
        "show_date_time": "2019-08-07 10:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 3,
        "id": 4,
        "movie_id": 1,
        "show_date_time": "2019-08-06 10:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "id": 6,
        "movie_id": 2,
        "show_date_time": "2019-08-06 12:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "id": 7,
        "movie_id": 2,
        "show_date_time": "2019-08-04 12:00:00",
        "price": 20000
    }
]

ticket = [
    {
        "payment_method": "mm",
        "id": 1,
        "seat_number": "h23",
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "id": 2,
        "seat_number": "h34",
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "id": 9,
        "seat_number": "d45",
        "user_id": 1,
        "showtime_id": 1
    },
    {
        "payment_method": "mm",
        "id": 3,
        "seat_number": "h23",
        "user_id": 1,
        "showtime_id": 2
    },
    {
        "payment_method": "mm",
        "id": 4,
        "seat_number": "a12",
        "user_id": 1,
        "showtime_id": 4
    },
    {
        "payment_method": "mm",
        "id": 5,
        "seat_number": "g34",
        "user_id": 1,
        "showtime_id": 4
    }
]
