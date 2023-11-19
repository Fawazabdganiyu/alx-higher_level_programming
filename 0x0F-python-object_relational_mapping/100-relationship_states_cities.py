#!/usr/bin/python3
"""
Module Name: 100-relationship_states_cities.py
Description: This is a script that creates `State` "California" with the `City`
             "San Francisco" from the database `hbtn_0e_100_usa`
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost/{database}'

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California',
                       cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()

    session.close()
