#!/usr/bin/python3
#use filter to find condition then print


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
    states = session.query(State).filter_by(name=argv[4]).first()

    if states is not None:
        print(states.id)
    else:
        print('Not found')

    session.close()
