#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user_name= argv[1]
    pass_word = argv[2]
    data_base= argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=pass_word, db=data_base)

    mapi = db.cursor()
    mapi.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = mapi.fetchall()
    for data in rows:
        print(data)

    mapi.close()
    db.close()
