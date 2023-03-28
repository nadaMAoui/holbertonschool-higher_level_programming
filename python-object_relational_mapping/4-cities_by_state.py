#!/usr/bin/python3
"""lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities\
             JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
se()
