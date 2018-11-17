import unittest
from warmup1 import *

class Warmup1Tests(unittest.TestCase):

    def test_diff21(self):
        self.assertEqual(diff21(19),2)
        self.assertEqual(diff21(10),11)
        self.assertEqual(diff21(21),0)

    def test_parrot_trouble(self):
        self.assertEqual(parrot_trouble(True, 6),True)
        self.assertEqual(parrot_trouble(True, 7),False)
        self.assertEqual(parrot_trouble(False, 6),False)

    def test_makes10(self):
        self.assertEqual(makes10(9, 10),True)
        self.assertEqual(makes10(9, 9),False)
        self.assertEqual(makes10(1, 9),True)

    def test_near_hundred(self):
        self.assertEqual(near_hundred(93),True)
        self.assertEqual(near_hundred(90),True)
        self.assertEqual(near_hundred(89),False)


if __name__ == '__main__':
    unittest.main()
