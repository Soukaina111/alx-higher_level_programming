#!/usr/bin/python3
"""
This script displays all City objects from the database
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user_name, pass_word, data_base))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
