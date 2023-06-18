#!/usr/bin/python3
"""Retriving a specific item specified in the command line and
   preventing the possibility of injections
   usage: ./2-my_filter_states.py <mysql username>
                                  <mysql password>
                                  <database name>
                                  <state name searched>"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE binary %s
                 ORDER BY id ASC""", (argv[4].strip("'"),))
    query_rows = cur.fetchall()
    [print(row) for row in query_rows]
