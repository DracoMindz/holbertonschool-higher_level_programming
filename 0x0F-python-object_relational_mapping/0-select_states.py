#!/usr/bin/python3
import MySQLdb
import sys
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
