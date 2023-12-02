#!/usr/bin/python3
def no_c(my_string):
	copy = my_string[:]
        for i in copy:
                if i == 'c' or i == 'C':
                    copy.remove(i)
	return ("".join(copy))
