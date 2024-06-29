#!/usr/bin/python3
""" A script that takes in the name of
    a state as an argument and lists
    all cities of that state """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                 host="localhost", port=3306, db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM cities \
                    WHERE state_id = (SELECT id FROM states \
                    WHERE name = %s) ORDER BY cities.id ASC", (argv[4],))
    names = cursor.fetchall()

    print(", ".join(name[0] for name in names))

    cursor.close()
    connection.close()
