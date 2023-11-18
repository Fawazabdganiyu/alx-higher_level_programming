#!/usr/bin/python3
"""
Module Name: 11-model_state_insert.py
Description: This script adds the `State` object "Louisiana"
             to the database `hbtn_0e_6_usa`
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost/{database}'

    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a `State` instance
    state = State(name='Louisiana')

    # Add the state to the table
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
