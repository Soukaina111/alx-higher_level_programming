#!/usr/bin/python3
''' MyList class for second task.'''


class MyList(list):
    ''' MyList class.'''
    def print_sorted(self):
        '''Method to print ordered list.'''
        print(sorted(self))
