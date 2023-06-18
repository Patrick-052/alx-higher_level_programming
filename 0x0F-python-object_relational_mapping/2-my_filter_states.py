#!/usr/bin/python3
"""Retriving a specific item specified in the command line"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    [print(row) for row in query_rows if row[1] == argv[4]]
