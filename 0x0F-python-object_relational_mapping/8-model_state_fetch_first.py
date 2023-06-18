#!/usr/bin/python3
"""Retrieving all state objects from the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
             "mysql+mysqldb://{}:{}@localhost/{}"
             .format(argv[1], argv[2], argv[3]),
             pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
