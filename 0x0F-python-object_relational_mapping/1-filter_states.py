#!/usr/bin/python3

""" 
This script that lists all states from the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]

    db = MySQLdb.connect(host = "localhost", port = 3306, user = user_name, passwd = pass_word, db = data_base)
    mapi = db.cursor()
    mapi.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = mapi.fetchall()
    for data in rows:
        print(data)
    mapi.close()
    db.close()
