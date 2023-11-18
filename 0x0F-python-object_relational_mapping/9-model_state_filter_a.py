#!/usr/bin/python3
"""
Module Name: 9-model_state_filter_a.py
Description: This is a script that lists all `State` objects that contain
             the letter "a" from the database `hbtn_0e_6_usa`
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost/{database}'

    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).all()

    # Display
    for state in query:
        print(f'{state.id}: {state.name}')
