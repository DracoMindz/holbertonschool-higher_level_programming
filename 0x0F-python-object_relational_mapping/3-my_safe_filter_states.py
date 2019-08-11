#!/usr/bin/python3
# Using States Data
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE `name` LIKE BINARY '{}'
                ORDER BY id ASC""".format(sys.argv[4]))
    query_row = cur.fetchall()
    for row in query_row:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    conn.close()
