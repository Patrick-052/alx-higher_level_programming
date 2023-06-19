#!/usr/bin/python3
"""Changing the value of an item in the database"""

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

    csi = session.query(State).filter(State.name.ilike("%a%")).all()
    for state in csi:
        session.delete(state)
    session.commit()
