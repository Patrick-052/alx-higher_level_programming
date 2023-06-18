#!/usr/bin/python3
"""Retriving items from cities from the database and joininig
   them to items in states
   usage: ./4-cities_by_state.py <mysql username>
                                 <mysql password>
                                 <database name>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    cs = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = cs.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
              FROM cities JOIN states ON
              cities.state_id = states.id ORDER BY cities.id ASC""")
    qr = c.fetchall()
    [print(r) for r in qr]
