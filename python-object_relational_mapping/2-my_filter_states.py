#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=database)
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE '{}'COLLATE latin1_general_cs\
                ORDER BY states.id".format(argv[4]))"
    cursor.execute(query, ('%' + state_name + '%',))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

