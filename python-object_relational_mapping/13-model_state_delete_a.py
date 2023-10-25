#!/usr/bin/python3
""" Script that adds state louisiana
to database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                           @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()
