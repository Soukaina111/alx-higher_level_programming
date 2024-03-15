import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    engine = create_engine(f'mysql://{mysql_username}:{mysql_password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name == searched).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
