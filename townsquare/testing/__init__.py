"""
The testing package provides test boilerplate to avoid
writing the same code in tests. Use it extensively.

"""

from flask_testing import TestCase
from townsquare import TownSquare


class TownSquareTestCase(TestCase):

    def create_app(self):

        return TownSquare.create_app('testing')

