#!/usr/bin/python3
"""
This script use SQLAlchemy  to add a new object
"""

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

    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
