#!/usr/bin/python3

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
    entryfirst = session.query(State).order_by(State.id).first()

    if entryfirst is not None:
        print("{}: {}".format(entryfirst.id, entryfirst.name))
    else:
        print('Nothing')

    session.close()
