#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

"""
This script is a module defining the City
class, which represents cities in a database.
"""


class City(Base):
    """
    This class represents a city in the database.
    
    It inherits from the ``Base`` class, which provides
    the base functionality for SQLAlchemy models.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
