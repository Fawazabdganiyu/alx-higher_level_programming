#!/usr/bin/python3
"""
Module Name: 1-filter_states.py
Description: This module provides a script that lists all `states` with a name
             starting with "N" from the database `hbtn_0e_0_usa`
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, password, database = argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
