#!/usr/bin/python3
""" This script lists the cities of the database """
import MySQLdb
from sys import argv


if __name__ == '__main__':

	user_name= argv[1]
	pass_word = argv[2]
	data_base= argv[3]

	db= MySQLdb.connect(host="localhost", port = "3306", user=user_name, passwd= pass_word,database=data_base)

	mapi = db.cursor();
        mapi.execute("SELECT *  FROM cities INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")


	rows = mapi.fetchall();
	for i in rows:
		print(i)

	mapi.close();
	db.close();
