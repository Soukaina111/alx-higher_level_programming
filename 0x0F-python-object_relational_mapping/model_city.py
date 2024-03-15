#!/usr/bin/python3
"""
This script defines a City class using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")

if __name__ == '__main__':
    engine = create_engine('mysql://username:password@localhost:3306/hbtn_0e_4_usa')
    Base.metadata.create_all(engine)
