#!/usr/bin/python3
"""
This script use SQLAlchemy to add an object named  “Louisiana” 
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')

    session.add(new)

    session.commit()

    print("{}: {}".format(new.id, new.name))

    session.close()
