#!/usr/bin/python3
""" A script that takes in an argument
    and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                 host="localhost", port=3306, db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                    ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
