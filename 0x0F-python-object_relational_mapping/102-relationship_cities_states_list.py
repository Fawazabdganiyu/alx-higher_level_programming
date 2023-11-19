#!/usr/bin/python3
"""
Module Name: 102-relationship_cities_states_list.py
Description: This is a script that lists all `City` objects with `state`
             relationship contained in the database `hbtn_0e_101_usa`
"""
import sys
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, database)

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id).all()

    # Display
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
