#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306/
    {}""".format(sys.argv[1], sys.argv[2], sys.argv[3]),
                 pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()

    Rt = session.query(State).join(State.City)\
                .filter(City.state_id == State.id).order_by(City.id).all()
    [print("{}: ({}) {}".format(i[1], i[2], i[4]))
     for i in Rt]
