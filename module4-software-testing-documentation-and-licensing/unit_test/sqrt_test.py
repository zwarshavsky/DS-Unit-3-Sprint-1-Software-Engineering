"""Testing file for square root functions"""

import unittest 
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt
from math import sqrt
    


# our class for square root functions
class SqrtTests(unittest.TestCase):
    """"Tests for square root functions"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)
    def test_sqrt2(self):
        self.assertEqual(newton_sqrt(2),1.414213562373095)

class OtherTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()