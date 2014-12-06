"""
The testing package provides test boilerplate to avoid
writing the same code in tests. Use it extensively.

"""

from flask_testing import TestCase
from townsquare import TownSquare
from townsquare.db import db


class TownSquareTestCase(TestCase):

    def setUp(self):
        db.create_all()
        
        return super(TownSquareTestCase, self).setUp()
    
    def tearDown(self):
        db.drop_all()

        return super(TownSquareTestCase, self).tearDown()

    def create_app(self):

        return TownSquare.create_app('testing')

