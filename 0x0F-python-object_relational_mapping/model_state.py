#!/usr/bin/python3
"""
This script is  Using module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql://username:password@localhost:3306/hbtn_0e_4_usa')
    Base.metadata.create_all(engine)
