#!/usr/bin/python3
"""
Module Name: 12-model_state_update_id_2.py
Description: This script changes the name of a `State` object
             from the database `hbtn_0e_6_usa`
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

    query = session.query(State).filter_by(id=2).first()
    query.name = "New Mexico"
    session.commit()

    session.close()
