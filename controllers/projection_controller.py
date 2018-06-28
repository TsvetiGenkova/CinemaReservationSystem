from prettytable import PrettyTable
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.create_db import Movie
from database.create_db import Projection

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()

class ProjectionController:

    @classmethod
    def add_new_projection(cls, movie_id, type, date, time):        
        movies = session.query(Projection.movie_id).filter().all()
        if movie_id in movies:
            raise ValueError("There is movie with this id")

        session.add(Projection(movie_id=movie_id, type=type, date=date, time=time))
        session.commit()