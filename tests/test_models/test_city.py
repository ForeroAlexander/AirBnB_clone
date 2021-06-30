#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    '''
        Testing city class
    '''

    def test_City_inheritance(self):
        '''
            testing City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        '''
            Testing city atrributes
        '''
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
