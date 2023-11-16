#!/usr/bin/python3
"""
Module name: 0-select_states.py
Description: This module provides a script that lists all `states`
             from the database `hbtn_0e_0_usa`
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    hostname = 'localhost'
    port = 3306
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host=hostname, port=port, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
