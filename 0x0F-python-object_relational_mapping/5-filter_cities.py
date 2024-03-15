#!/usr/bin/python3
"""
This script lists the cities of state passed as an argv
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]
    state_n = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=pass_word, db=data_base)

    mapi = db.cursor()
    mapi.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [state_n])

    rows = mapi.fetchall()
    ListA = []
    for i in rows:
        ListA.append(i[1])
    print(", ".join(ListA))

    mapi.close()
    db.close()
