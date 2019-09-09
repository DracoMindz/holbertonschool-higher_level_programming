#!/usr/bin/python3
"""Class contains class definition of a City and an instance Base"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class State, attributes: id, name"""

    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
