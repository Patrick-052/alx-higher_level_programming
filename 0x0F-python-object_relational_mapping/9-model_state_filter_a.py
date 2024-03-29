#!/usr/bin/python3
"""Retrieving state objects from the database that contain
   (a) iin their name"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
             "mysql+mysqldb://{}:{}@localhost/{}"
             .format(argv[1], argv[2], argv[3]),
             pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).filter(State.name.ilike("%a%"))\
                    .order_by(State.id).all()
    [print("{}: {}".format(state.id, state.name)) for state in states]
