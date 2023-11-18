#!/usr/bin/python3
"""
Module Name: 10-model_state_my_get.py
Description: This script prints the `State` object with the `name` passed
             as argument from the database `hbtn_0e_6_usa`
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database, state_name = sys.argv[1:]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost/{database}'

    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name).one_or_none()

    # Display
    if query:
        print(query.id)
    else:
        print('Not found')
