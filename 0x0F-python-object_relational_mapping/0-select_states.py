#!/usr/bin/python3
"""
Module name: 0-select_states.py
Description: This module provides a script that lists all `states`
             from the database `hbtn_0e_0_usa`
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, password, database = argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
