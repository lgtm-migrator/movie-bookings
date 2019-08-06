from apps.middlewares.validation import ValidationError
from .fixtures import *
from models import *
from collections import OrderedDict


class NotFound(Exception):
    pass


tables = [Users, CinemaHall, Movie, ShowTime, Seat, Ticket]


def create_tables(db):
    for table in tables:
        string = table.create()
        with db.cursor(commit=True) as cursor:
            cursor.execute(string)


def find_or_404(db, model, **kwargs):
    query = model.find('OR', **kwargs)
    results = db.execute(query, commit=True)
    if not results:
        result = []
        for item, value in kwargs.items():
            result.append(f"{item} = '{value}'")
        raise ValidationError('error', status_code=400, payload={
                              'message': "{} not found".format(', '.join(result))})
    return results


def seed_data(db):
    db.drop_all()
    create_tables(db)
    fixtures = OrderedDict({
        'user': Users,
        'cinemahall': CinemaHall,
        'movie': Movie,
        'showtime': ShowTime,
        'seat': Seat,
        'ticket': Ticket,
    })
    for fixture, model in fixtures.items():
        query = model().insert_query(eval(fixture))
        db.execute(query, named=True, commit=True)