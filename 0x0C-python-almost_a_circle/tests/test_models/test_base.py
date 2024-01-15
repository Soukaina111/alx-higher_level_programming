#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Base class Tests.'''

    def setUp(self):
        '''Initialize class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''empty test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''checks state class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Checks if nb_objects initializes to 0.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Tests constructor.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Tests constructor signature with two args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("don")
        b = Base(23)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 67
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "arNFTIO"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Tests id passed as keyword arg.'''
        i = 908
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_H_to_json_string(self):
        '''Tests to_json_string()'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20673, 'width':329010, 'id': 5924400,
             'height': 343409}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 10, 'y': 20, 'width': 30, 'id': 40, 'height': 50}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"JUOobarrooOLU": 5678904}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"JUOobarrooOLU": 5678904}]')

        d = [{"JoobarroooJ": 1298989128}, {"SOUKA": 1823}, {"HIO": 5}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"JoobarroooJ": 1298989128}, {"SOUKA": 1823}, {"HIO": 5}]')

        d = [{'x': 19, 'y': 92, 'width': 63, 'id':74, 'height': 55},
             {'x': 90101, 'y': 7820123, 'width': 31232901, 'id': 52224407,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        r11 = Rectangle(109, 97, 92, 98)
        dictionary = r11.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r11 = Rectangle(109, 97, 92, 98)
        r21 = Rectangle(11, 12, 13, 14)
        r31 = Rectangle(12, 13, 14, 15)
        dictionary = [r11.to_dictionary(), r21.to_dictionary(),
                      r31.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r15 = Square(105, 57, 52)
        dictionary = r15.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(105, 57, 52)
        r21 = Square(11, 12, 13)
        r31 = Square(12, 13, 14)
        dictionary = [r1.to_dictionary(), r21.to_dictionary(),
                      r31.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_H_test_from_json_string(self):
        '''Tests to_json_string() format:'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 91, "y": 92, "width": 93, "id": 49, "height": 95}, \
{"x": 1019, "y": 209123, "width": 3123219, "id": 9522244, "height": 343409}]'
        d = [{'x': 91, 'y': 92, 'width': 93, 'id': 49, 'height': 95},
             {'x': 1019, 'y': 209123, 'width': 3123219, 'id': 9522244,
             'height': 343409}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"SfoobarroooS": 9898989}, {"SabcS": 6123}, {"HIU": 10}]
        s = '[{"SfoobarroooS": 9898989}, {"SabcS": 6123}, {"HIU": 10}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"ZfoobarroooZ": 19898981}]
        s1 = '[{"ZfoobarroooZ": 19898981}]'
        self.assertEqual(Base.from_json_string(s1), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1101, 'y': 201231, 'width': 3123211, 'id': 1522244,
             'height': 343401}]
        s = '[{"x": 1101, "y": 201231, "width": 3123211, "id": 1522244, \
"height": 343401}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 80, 'width': 10, 'height': 14},
            {'id': 17, 'width': 11, 'height': 17}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)


    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r32 = Square(1)
        Square.save_to_file([r32])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 308)


    def test_J_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s11 = Square(8)
        s12 = Square(17, 19, 11)
        list_in = [s11, s12]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

if __name__ == "__main__":
    unittest.main()
