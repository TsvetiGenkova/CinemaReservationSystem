from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

class Projection(Base):
    __tablename__ = "projection"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id))
    movie = relationship(Movie, backref="projection")
    type = Column(String)
    date = Column(String)
    time = Column(String)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class Reservation(Base):
    __tablename__ = "reservation"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    projection_id = Column(Integer, ForeignKey(Projection.id))
    row = Column(Integer)
    col = Column(Integer)


engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
