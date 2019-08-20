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
    cur.execute("SELECT cities.name\
                FROM cities \
                JOIN states ON (cities.state_id = states.id)\
                WHERE states.name = '{}' \
                ORDER BY cities.id ASC".format(sys.argv[4]))
    citynames = ', '.join([row[0]for row in cur.fetchall()])
    print(citynames)
    cur.close()
    conn.close()
