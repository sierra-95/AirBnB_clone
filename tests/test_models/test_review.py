#!/usr/bin/python3
'''
tests for review model
'''

from models.review import Review
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = Review()
    my_model.name = "laResena"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, Review)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(
            self.my_model.created_at, datetime)
        self.assertIsInstance(
            self.my_model.updated_at, datetime)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.place_id), str)
        self.assertEqual(type(self.my_model.user_id), str)
        self.assertEqual(type(self.my_model.text), str)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(type(self.my_model.created_at), datetime)

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
        self.assertEqual(hasattr(self.my_model, 'place_id'), True)
        self.assertEqual(hasattr(self.my_model, 'user_id'), True)
        self.assertEqual(hasattr(self.my_model, 'text'), True)

    def test_doc(self):
        '''test for doc'''
        self.assertIsNotNone(Review.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
