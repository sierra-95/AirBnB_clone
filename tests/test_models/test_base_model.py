#!/usr/bin/python3
'''Unittest module for Base Model Class'''

import uuid
from datetime import datetime, date, time
import models
from models.base_model import BaseModel
import json
import unittest


class TestBaseModel(unittest.TestCase):
    '''Unittest module for Base Model Class'''
    def setUp(self):
        """ create instances of Base and setup tests"""
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model2 = BaseModel()

    def teardown(self):
            """End tests and del instances"""
            del self.my_model
            del self.my_model2
            try:
                os.remove("file.json")
            except:
                pass

    def test_instantiation(self):
        '''Unittest module for Base Model Class'''
        self.assertEqual(str(type(self.my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(issubclass(type(self.my_model), BaseModel))

    def test_unique_id(self):
        '''Check unique Id por instances'''
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str_check(self):
        '''Test if the output is ok'''
        str1 = "[BaseModel] ({}) {}".format(self.my_model.id,
                                            self.my_model.__dict__)
        self.assertEqual(str1, str(self.my_model))

    def test_save(self):
        '''Test if is saving the changes'''
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict(self):
        '''Test to dictionary'''
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        dict1 = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'BaseModel')
        self.assertEqual(dict1['updated_at'],
                         self.my_model.updated_at.strftime(d_format))
        self.assertEqual(dict1['created_at'],
                         self.my_model.created_at.strftime(d_format))
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['created_at']), str)

    def test_dict_to_BaseModel(self):
        '''Test to BaseModel'''
        dict1 = self.my_model.to_dict()
        new = BaseModel(**dict1)
        self.assertTrue(isinstance(new, BaseModel))
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.name, "Holberton")
        self.assertEqual(new.id, self.my_model.id)
        self.assertEqual(new.updated_at, self.my_model.updated_at)
        self.assertEqual(new.created_at, self.my_model.created_at)
        self.assertNotEqual(new, self.my_model)

    def test_checking_docstring_BaseModel(self):
        """ Test if all docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

if __name__ == '__main__':
    unittest.main()
