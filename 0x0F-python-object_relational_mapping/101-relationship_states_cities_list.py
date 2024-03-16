#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    states = session.query(State).order_by(State.id).all()

    for st in states:
        print(f'{st.id}: {st.name}')
        for city in st.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
