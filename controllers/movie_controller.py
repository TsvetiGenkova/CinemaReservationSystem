from datetime import datetime
from prettytable import PrettyTable
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.create_db import Movie
from database.create_db import Projection
from database.session_manager import SessionManager

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()

class MovieController():

    @classmethod
    def create_movie(cls, name, rating):
        if int(rating) < 0:
            raise ValueError("Rating must be positive number")
        
        all_movies_names = session.query(Movie.name).filter().all()
        if name in all_movies_names:
            raise ValueError("There is a movie with that name already")
        
        session.add(Movie(name=name, rating=rating))
        session.commit()

    @classmethod
    def get_movie_name(cls, movie_id):
        return session.query(Movie.name).filter(Movie.id == movie_id).all()

    @classmethod
    def show_all_movies(cls):
        table = PrettyTable(["id", "movie_name", "movie_rating"])
        all_movies = session.query(Movie.id, Movie.name, Movie.rating).filter().all()
        for i in all_movies:
            table.add_row([i[0], i[1], i[2]])
        return table

    @classmethod
    def show_movie_projections(cls, movie_id, date=None):
        if date != None:
            present = datetime.now()
            if datetime(date) < present:
                raise ValueError("The date shuld be in the future")
        table = PrettyTable(["id", "type", "date", "time"])
        projections = session.query(Projection.id, Projection.type, Projection.date, Projection.time).filter(Projection.movie_id == movie_id).all()
        for row in projections:
            table.add_row([row[0], row[1], row[2], row[3]])
        return table