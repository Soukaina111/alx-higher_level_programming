#!/usr/bin/python3
""" This script that lists all states Starting with N safely """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]
    search = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=pass_word,
        db=data_base,
        charset="utf8"
    )
    mapi = db.cursor()

    query = "SELECT * FROM states WHERE BINARY\
            name  =%s ORDER BY states.id ASC"

    mapi.execute(query, (search,))

    rows = mapi.fetchall()

    for data in rows:
        print(data)

    mapi.close()
    db.close()
