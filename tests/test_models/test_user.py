#!/usr/bin/python3
'''
tests for user model
'''

from models.user import User
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = User()
    my_model.name = "jhonatan"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, User)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(
            self.my_model.created_at, datetime)
        self.assertIsInstance(
            self.my_model.updated_at, datetime)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.email), str)
        self.assertEqual(type(self.my_model.password), str)
        self.assertEqual(type(self.my_model.first_name), str)
        self.assertEqual(type(self.my_model.last_name), str)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_has_attr(self):
        '''test for attributes'''
        self.assertEqual(hasattr(self.my_model, 'email'), True)
        self.assertEqual(hasattr(self.my_model, 'password'), True)
        self.assertEqual(hasattr(self.my_model, 'first_name'), True)
        self.assertEqual(hasattr(self.my_model, 'last_name'), True)
        self.assertEqual(hasattr(self.my_model, 'id'), True)
        self.assertEqual(hasattr(self.my_model, 'updated_at'), True)
        self.assertEqual(hasattr(self.my_model, 'created_at'), True)
        self.assertEqual(hasattr(self.my_model, '__class__'), True)

    def test_doc(self):
        '''test for doc'''
        self.assertIsNotNone(User.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
