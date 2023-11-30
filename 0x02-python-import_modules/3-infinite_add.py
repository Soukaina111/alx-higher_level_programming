#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

i = 0
summ = 0
for i in range(1, argc + 1):
    summ += int(sys.argv[i])

print("{:d}".format(summ))
