#!/usr/bin/python3
""" This script that lists all states Starting with N safely """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]
    search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=pass_word, db=data_base)

    mapi = db.cursor()

    query = "SELECT * FROM states WHERE BINARY =%s ORDER BY id ASC"

    mapi.execute(query, (search,))

    rows = cur.fetchall()

    for data in rows:
        print(row)

    mapi.close()
    db.close()
