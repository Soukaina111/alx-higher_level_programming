#!/usr/bin/python3
'''Base class.'''
from json import dumps, loads


class Base:
    '''Base class.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id !=None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

 @staticmethod
    def to_json_string(list_dictionaries):
        '''serailization.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''deserialization.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves json object to file with encoding UTF-8.'''
        if list_objs != None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fi:
            fi.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''brings string from file and deserailize it.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fi:
            return [cls.create(**d) for d in cls.from_json_string(fi.read())]


