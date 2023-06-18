#!/usr/bin/python3
"""Retriving cities from cities.table from the database belonging
   to a particular state parsed in the command line
   usage: ./5-filter_cities.py <mysql username>
                               <mysql password>
                               <database name>
                               <state name>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    cs = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = cs.cursor()
    c.execute("""SELECT cities.name FROM cities
              JOIN states ON cities.state_id = states.id
              WHERE states.name = %s ORDER BY cities.id ASC""", (argv[4],))
    qr = c.fetchall()
    [print(r) for r in qr]
