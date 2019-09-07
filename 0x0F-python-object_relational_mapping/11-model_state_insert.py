#!/usr/bin/python3
# add a new state object Louisiana


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    # the function takes in thre arguments

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    entry = State(name='Louisiana')
    session.add(entry)
    session.commit()

    print("{}".format(entry.id))
