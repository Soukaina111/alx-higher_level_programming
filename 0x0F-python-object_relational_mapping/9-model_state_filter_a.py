#!/usr/bin/python3
"""
Using SQLAlchemy this script displays all State objects having letter "a"
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id.asc()).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
