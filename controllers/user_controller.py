import re
import hashlib
from .decorators import log, validate_password
from database.create_db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()

class UserController:
    Session = sessionmaker()
    session = Session()

    
    @classmethod
    @log("reservations_log.txt")
    @validate_password()
    def register(cls, user_name, password):
        hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            user_name.encode(),
            10000
            ).hex()
        session.add(User(username=user_name, password=str(hash)))
        session.commit()

    @classmethod
    def login(cls, user_name, password):
        hashed_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            user_name.encode(),
            10000
            ).hex()
        user_pass = session.query(User.password).filter(User.username == user_name).one()
        if user_pass == []:
            raise ValueError("Wrong username")
        user = session.query(User.id, User.username).filter(User.username == user_name, User.password == str(hashed_pass)).one()
        print(user)
        if user:
            return user
        else:
            return False
        
