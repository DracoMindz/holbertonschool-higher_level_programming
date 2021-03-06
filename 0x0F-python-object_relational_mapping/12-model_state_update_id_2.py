#!/usr/bin/python3
# changes state object with id = 2 to New Mexico
# script connects via sqlachemy to mysql db local host port 3306


import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    # the function takes in three arguments

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State)\
        .filter(State.id == 2).update({State.name: "New Mexico"})

    session.commit()
