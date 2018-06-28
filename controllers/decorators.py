from datetime import datetime
from functools import wraps
import re
from database.create_db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()


def log(file_name):
    def accepter(func):
        def decorator(*args):
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            to_write = f"Reservation was made at {time}"
            with open(file_name, "w") as f:
                f.write(to_write)
            return func(*args)
        return decorator
    return accepter


def validate_password():
    def accepter(func):
        def decorator(*args, **kwargs):  
            all_user_names = session.query(User.username).filter().all()
            user_name = args[0]
            password = args[1]
            if user_name in all_user_names:
                raise ValueError("There is a user with that name already")
            elif len(password) < 8:
                raise ValueError("Pasword should be at least 8 symbols long")
            elif not any(x.isupper() for x in password):
                raise ValueError("Pasword should contain a capital letter")
            elif not re.match(r'^\w+$', password):
                raise ValueError("Pasword should contain a special symbol")
            else:
                return func(*args, **kwargs)
        return decorator
    return accepter