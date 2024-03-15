#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

	user_name= argv[1]
	pass_word = argv[2]
	data_base= argv[3]
	searched = argv[4]

	db= MySQLdb.connect(host="localhost", port = "3306", user=user_name, passwd= pass_word,database=data_base)

	mapi = db.cursor();

	 query = "SELECT * FROM cities WHERE state = %s ORDER BY id ASC"
   	 mapi.execute(query, (searched,))

	rows = mapi.fetchall();
	for i in rows:
		print(i)

	mapi.close();
	db.close();
