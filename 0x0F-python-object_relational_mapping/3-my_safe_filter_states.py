#!/usr/bin/python3
"""
Module Name: 3-my_safe_filter_states.py
Description: A script that matches the `name` in the `state` table of
             `hbtn_0e_0_usa` provided as part of the arguments and
             safe from MySQL injections

"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, password, database, state_name = argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    query = (
        """SELECT * FROM states \
        WHERE name LIKE BINARY %s \
        ORDER BY id ASC"""
    )
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
