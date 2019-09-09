#!/usr/bin/python3
# Python file model_city.py that contains the class definition of a City
# script connects via sqlachemy to mysql db local host port 3306


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    # the function takes in three arguments

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    request = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in request:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
