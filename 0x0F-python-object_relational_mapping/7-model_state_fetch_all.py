#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    data_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                                format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(data_engine)
    Session = sessionmaker(bind=data_engine)
    session = Session()

    for entry in session.query(State).order_by(State.id):
        print("{}: {}".format(entry.id, entry.name))

    session.close()
