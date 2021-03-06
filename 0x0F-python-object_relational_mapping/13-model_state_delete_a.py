#!/usr/bin/python3
"""
Change: delete all State objects with an a in the name
script connects via sqlachemy to mysql db local host port 3306
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    # the function takes in three arguments

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create variable for query search
    # filter out the states that contain and 'a'
    session.query(State).filter(State.name.contains('%a%').all()) \
        .delete(state)

    session.flush
    session.commit
    session.close
