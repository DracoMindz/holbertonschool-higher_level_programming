#!/usr/bin/python3
# add a new state


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    entry = State(name='Louisiana')
    session.add(entry)
    entryfirst = session.query(State).filter_by(name='Louisiana').first()
    print(entryfirst.id)
    session.commit
