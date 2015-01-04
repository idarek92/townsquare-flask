import unittest
from townsquare.common import assert_instance

class A(object):
    pass

class B(A):
    pass

class TestAssertInstance(unittest.TestCase):

    def test_instance(self):
        self.assertIsNone(assert_instance(1, int))

    def test_not_instance(self):
        self.assertRaises(TypeError, assert_instance, 1, bool)

    def test_inheritance(self):
        # testing that we can inherit and pass argument still
        self.assertIsNone(assert_instance(A(), A))
        self.assertIsNone(assert_instance(B(), A))

        self.assertRaises(TypeError, assert_instance, A(), B)

