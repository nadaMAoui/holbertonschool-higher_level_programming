#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query, ('%' + state_name + '%',))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
