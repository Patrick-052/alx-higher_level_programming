#!/usr/bin/python3
"""Mapping city class to cities table in the database"""

from model_state import State
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Inherits from Base and defines the following class attributes:
        __tablename__ => defines name of the table
        id => represents a column of an auto-generated, unique integer,
        can't be null and is a primary key
        name => represents a column of a string of 128 characters and
        can't be null
        state_id => represents a column of an integer, can't be null
        and is a foreign key to states.id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
