#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

        user_name= argv[1]
        pass_word = argv[2]
	data_base= argv[3]
	searched = argv[4]

	db= MySQLdb.connect(host="localhost", port = "3306", user=user_name, passwd= pass_word,db=data_base)

	mapi = db.cursor();
        mapi.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", searched)

        rows = mapi.fetchall()
        listA = []
        for i in rows:
            listA.append(i[1])
        print(", ".join(listA))

	mapi.close();
	db.close();
