#!/usr/bin/python3
"""
Module Name: 5-filter_cities.py
Description: A script that lists all `cities` by a state passed
             as an argument using the database `hbtn_0e_4_usa`
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, database, state_name = argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    query = (
        "SELECT c.name \
           FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id \
                WHERE s.name = %s \
          ORDER BY c.id"
        )
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    cities_in_the_state = []
    for row in rows:
        cities_in_the_state.append(row[0])

    cities = ', '.join(cities_in_the_state)
    print(cities)

    cur.close()
    conn.close()
