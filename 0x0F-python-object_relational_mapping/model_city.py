#!/usr/bin/python3
"""
This script defines a City class using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
