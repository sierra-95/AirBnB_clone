#!/usr/bin/python3
'''
tests for city model
'''

from models.city import City
import unittest


class TestState(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = City()

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, City)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.state_id), str)
        self.assertEqual(type(self.my_model.name), str)

    def test_has_attr(self):
        '''test for attributes'''
        self.assertEqual(hasattr(self.my_model, 'state_id'), True)
        self.assertEqual(hasattr(self.my_model, 'name'), True)

    def test_doc(self):
        '''test for doc'''
        self.assertIsNotNone(City.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
