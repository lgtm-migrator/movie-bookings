user = [
    {
        "email": "peter@gmail.com",
        "password": "sha256$UyheEiSQ$1e5b829d612f4134c0c4848804549652862e795245f5ed1de8c885a81953b3e1",
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
        "length": "2:30"
    },
    {

        "date_of_release": "2019-08-06 00:00:00",
        "name": "lord of rings",
        "category": "times",
        "rating": 5,
        "length": "2:30"
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
        "name": "a"
    },
    {
        "number": 3,
        "cinema_hall": 1,
        "name": "a"
    },
    {
        "number": 2,
        "cinema_hall": 1,
        "name": "b"
    },
    {
        "number": 4,
        "cinema_hall": 1,
        "name": "b"
    },
    {
        "number": 1,
        "cinema_hall": 2,
        "name": "c"
    },
    {
        "number": 4,
        "cinema_hall": 2,
        "name": "e"
    }
]

showtime = [
    {
        "cinema_hall": 1,
        "movie_id": 1,
        "show_date_time": "2019-08-09 08:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 1,
        "movie_id": 1,
        "show_date_time": "2019-08-07 00:00:00",
        "price": 30000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_date_time": "2019-08-07 00:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 1,
        "show_date_time": "2019-08-07 10:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 3,
        "movie_id": 1,
        "show_date_time": "2019-08-06 10:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_date_time": "2019-08-06 12:00:00",
        "price": 20000
    },
    {
        "cinema_hall": 2,
        "movie_id": 2,
        "show_date_time": "2019-08-04 12:00:00",
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
