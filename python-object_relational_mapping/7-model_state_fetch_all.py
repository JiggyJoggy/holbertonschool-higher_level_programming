#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                           @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session_maker = sessionmaker(bind=engine)
    Session = Session_maker()
    states = Session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
