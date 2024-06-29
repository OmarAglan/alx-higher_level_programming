#!/usr/bin/python3
""" Script that lists all State objects that contain the letter a
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                            @localhost:3306/{argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
