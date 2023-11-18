#!/usr/bin/python3
"""
Module Name: 7-model_state_fetch_all.py
Description: This is a script that lists all `State` objects from
             database hbtn_0e_6_usa
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

    query = session.query(State).order_by(State.id).all()

    # Display
    for state in query:
        print(f'{state.id}: {state.name}')
