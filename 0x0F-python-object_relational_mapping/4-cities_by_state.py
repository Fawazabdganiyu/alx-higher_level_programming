#!/usr/bin/python3
"""
Module Name: 4-cities_by_state.py
Description: A script that lists all `cities` from the database `hbtn_0e_4_usa`
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, database = argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    query = (
        "SELECT c.id, c.name, s.name \
           FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id \
          ORDER BY c.id"
        )
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
