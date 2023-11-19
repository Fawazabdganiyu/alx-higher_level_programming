#!/usr/bin/python3
"""
Module Name: 13-model_state_delete_a.py
Description: This script deletes all `State` object with a name containing
             "a" from the database `hbtn_0e_6_usa`
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

    query = session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()

    session.close()
