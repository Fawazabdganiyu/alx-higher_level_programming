#!/usr/bin/python3
"""
Module Name: 101-relationship_states_cities_list.py
Description: This is a script that lsits `State` objects and corresponding
             `City` objects, contained in the database `hbtn_0e_101_usa`
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, database)

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    # Display
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
