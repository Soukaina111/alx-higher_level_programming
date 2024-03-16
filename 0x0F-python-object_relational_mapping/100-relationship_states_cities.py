#!/usr/bin/python3
"""
This script adds the State object “California” with the City
“San Francisco” to the database hbtn_0e_100_usa
"""
 import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

if __name__ == "__main__":

   
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = City(name='San Francisco')
    new2 = State(name='California')
    new.cities.append(new2)
    session.add_all([new, new2])
    session.commit()
    session.close()
