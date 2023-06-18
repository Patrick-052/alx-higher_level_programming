#!/usr/bin/python3
"""class that is mapped to states table in the
   connected database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """inherits from Base and links to the table states
       it contains the following attributes:
        __tablename__ => defines name of the table
        id => represents a column of an auto-generated,
        unique integer, can't be null and is a primary key
        name => represents a column of a string with
        maximum 128 characters and can't be null
        """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
