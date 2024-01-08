#!/usr/bin/python3
"""
MyInt
"""


class MyInt(int):
    """opposite version of an integer!"""
    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, autre):
        """what was dif becomes equal"""
        return int(self) != autre

    def __ne__(self, autre):
        """what was equal is now dif"""
        return int(self) == autre
