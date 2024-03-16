#!/usr/bin/python3

"""
This script displays  all State objects and their
corresponding City objects
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        db_username, db_password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for st in states:
        print("{}: {}".format(st.id, st.name))
        for city in st.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
