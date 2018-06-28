from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cinema.db")

class SessionManager():
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = Session()