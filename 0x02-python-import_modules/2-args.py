#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

line = "{:d} argument"
count =len(sys.argv)-1
if count == 0
    line +=":s"
elif count == 1
    line += ':'
else
 line += 's:'
print(line.format(count))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
