#!/usr/bin/python3
"""
Module Name: 14-model_city_fetch_by_state.py
Description: This is a script that lists all `City` objects from
             database `hbtn_0e_6_usa` by state
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, passwd, database = sys.argv[1:]
    url = f'mysql+mysqldb://{user}:{passwd}@localhost/{database}'

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id).all()

    # Display
    for city in query:
        print(f'{city.states.name}: ({city.id}) {city.name}')

    session.close()
