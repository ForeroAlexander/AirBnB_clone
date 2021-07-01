#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def test_Review_inheritance(self):
        '''
            tests Review class BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Test Review class has place id, user id text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
