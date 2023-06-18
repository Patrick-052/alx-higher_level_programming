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
    cd = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = cd.cursor()
    c.execute("""SELECT * FROM cities
              INNER JOIN states ON cities.state_id = states.id
              ORDER BY cities.id ASC""")
    print(", ".join([r[2]
                    for r in c.fetchall()
                    if r[4] == argv[4]]))
