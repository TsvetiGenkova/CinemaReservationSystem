from database.create_db import Reservation
from database.create_db import Projection
from prettytable import PrettyTable
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_revervations_for_projection(projection_id):
    res = session.query(Reservation.row, Reservation.col).filter(Projection.id == projection_id).all()
    return res

class ReservationController:
    reservation = Reservation()

    @classmethod
    def add_new_reservation(cls, user, projection_id, row, col):
        if int(row) > 10 or int(row) <= 0:
            raise ValueError("Choose row between 1 and 10")
        
        if int(col) > 10 or int(col) <= 0:
            raise ValueError("Choose seat between 1 and 10")
        
        projections = session.query(Projection.movie_id).filter(Projection.id == projection_id).all()
        if not projections:
            raise ValueError("There is no projection with this id")

        reservations = get_revervations_for_projection(projection_id)
        if (row, col) in reservations:
           raise ValueError("This seat is taken")
        
        session.add(Reservation(user_id=user, projection_id=projection_id, row=row, col=col))

    @classmethod
    def finalize(cls):
        session.commit()

    @classmethod
    def get_free_seats(cls, projection_id):
        reservations =  get_revervations_for_projection(projection_id)
        return (100 - len(reservations))

    @classmethod
    def reservation_map(cls, projection_id):
        rows = 10
        cols = 10
        reservations =  get_revervations_for_projection(projection_id)
        cinema = []
        headers = [" " if x == 0 else x for x in range(rows + 1)]
        cinema.append(headers)
        for row in range(rows):
            cinema.append([str(row + 1) if col == 0 else "." for col in range(cols+1)])
        for i in reservations:
            cinema[i[0]][i[1]] = "X"
        table = PrettyTable()
        for row in cinema:
            table.add_row(row)
        return table.get_string(header=False, border=False)

