from .movie_controller import MovieController
from .reservation_controller import ReservationController
from .projection_controller import ProjectionController
from .user_controller import UserController
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()

class Controller():

    @classmethod
    def create_movie(cls, name, rating):
        return MovieController.create_movie(name, rating)

    @classmethod
    def show_movies(cls):
        return MovieController.show_all_movies()

    @classmethod
    def get_movie_name(cls, movie_id):
        return MovieController.get_movie_name(movie_id)

    @classmethod
    def show_projections(cls, movie_id, date=None):
        return MovieController.show_movie_projections(movie_id, date)

    @classmethod
    def show_cinema_map(cls, projection_id):
        return ReservationController.reservation_map(projection_id)

    @classmethod
    def get_free_seats(cls, projection_id):
        return ReservationController.get_free_seats(projection_id)

    @classmethod
    def add_new_reservation(cls,user, projection, row, col):
        return ReservationController.add_new_reservation(user, projection, row, col)

    @classmethod
    def finalize(cls):
        return ReservationController.finalize()

    @classmethod
    def register(cls, user_name, password):
        return UserController.register(user_name, password)

    @classmethod
    def login(cls, user_name, password):
        return UserController.login(user_name, password)