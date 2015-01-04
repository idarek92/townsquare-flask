import unittest
from townsquare.common import assertInstance

class A(object):
    pass

class B(A):
    pass

class TestAssertInstance(unittest.TestCase):

    def test_instance(self):
        self.assertIsNone(assertInstance(1, int))

    def test_not_instance(self):
        self.assertRaises(TypeError, assertInstance, 1, bool)

    def test_inheritance(self):
        # testing that we can inherit and pass argument still
        self.assertIsNone(assertInstance(A(), A))
        self.assertIsNone(assertInstance(B(), A))

        self.assertRaises(TypeError, assertInstance, A(), B)

