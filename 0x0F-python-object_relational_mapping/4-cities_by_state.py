#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                 host="localhost", port=3306, db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON states.id = cities.state_id \
                    ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
