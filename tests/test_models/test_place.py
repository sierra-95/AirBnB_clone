#!/usr/bin/python3
'''
tests for place model
'''

from models.place import Place
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = Place()
    my_model.name = "LaCasita"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, Place)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(
            self.my_model.created_at, datetime)
        self.assertIsInstance(
            self.my_model.updated_at, datetime)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.name), str)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(type(self.my_model.city_id), str)
        self.assertEqual(type(self.my_model.user_id), str)
        self.assertEqual(type(self.my_model.description), str)
        self.assertEqual(type(self.my_model.number_rooms), int)
        self.assertEqual(type(self.my_model.number_bathrooms), int)
        self.assertEqual(type(self.my_model.max_guest), int)
        self.assertEqual(type(self.my_model.price_by_night), int)
        self.assertEqual(type(self.my_model.latitude), float)
        self.assertEqual(type(self.my_model.longitude), float)
        self.assertEqual(type(self.my_model.amenity_ids), list)

    def test_has_attr(self):
        '''test for attributes'''
        self.assertEqual(hasattr(self.my_model, 'email'), False)
        self.assertEqual(hasattr(self.my_model, 'password'), False)
        self.assertEqual(hasattr(self.my_model, 'first_name'), False)
        self.assertEqual(hasattr(self.my_model, 'last_name'), False)
        self.assertEqual(hasattr(self.my_model, 'id'), True)
        self.assertEqual(hasattr(self.my_model, 'updated_at'), True)
        self.assertEqual(hasattr(self.my_model, 'created_at'), True)
        self.assertEqual(hasattr(self.my_model, '__class__'), True)
        self.assertEqual(hasattr(self.my_model, 'name'), True)
        self.assertEqual(hasattr(self.my_model, 'city_id'), True)
        self.assertEqual(hasattr(self.my_model, 'user_id'), True)
        self.assertEqual(hasattr(self.my_model, 'description'), True)
        self.assertEqual(hasattr(self.my_model, 'number_rooms'), True)
        self.assertEqual(hasattr(self.my_model, 'number_bathrooms'), True)
        self.assertEqual(hasattr(self.my_model, 'max_guest'), True)
        self.assertEqual(hasattr(self.my_model, 'price_by_night'), True)
        self.assertEqual(hasattr(self.my_model, 'latitude'), True)
        self.assertEqual(hasattr(self.my_model, 'longitude'), True)
        self.assertEqual(hasattr(self.my_model, 'amenity_ids'), True)

    def test_doc(self):
        '''test for doc'''
        self.assertIsNotNone(Place.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
