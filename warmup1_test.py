import unittest
from warmup1 import *


class Warmup1Tests(unittest.TestCase):

    def test_diff21(self):
        self.assertEqual(diff21(19), 2)
        self.assertEqual(diff21(10), 11)
        self.assertEqual(diff21(21), 0)

    def test_parrot_trouble(self):
        self.assertEqual(parrot_trouble(True, 6), True)
        self.assertEqual(parrot_trouble(True, 7), False)
        self.assertEqual(parrot_trouble(False, 6), False)

    def test_makes10(self):
        self.assertEqual(makes10(9, 10), True)
        self.assertEqual(makes10(9, 9), False)
        self.assertEqual(makes10(1, 9), True)

    def test_near_hundred(self):
        self.assertEqual(near_hundred(93), True)
        self.assertEqual(near_hundred(90), True)
        self.assertEqual(near_hundred(89), False)

    def test_pos_neg(self):
        self.assertTrue(pos_neg(1, -1, False), 'OK')
        self.assertTrue(pos_neg(-1, 1, False), 'OK')
        self.assertTrue(pos_neg(-4, -5, True), 'OK')

    def test_not_string(self):
        self.assertEqual(not_string('candy'), 'not candy')
        self.assertEqual(not_string('x'), 'not x')
        self.assertEqual(not_string('not bad'), 'not bad')

    def test_missing_char(self):
        self.assertEqual(missing_char('kitten', 1) , 'ktten')
        self.assertEqual(missing_char('kitten', 0) , 'itten')
        self.assertEqual(missing_char('kitten', 4) , 'kittn')

    def test_from_back(self):
        self.assertEqual(front_back('code') , 'eodc')
        self.assertEqual(front_back('a') , 'a')
        self.assertEqual(front_back('ab') , 'ba')

    def test_front3(self):
        self.assertEqual(front3('Java') , 'JavJavJav', 'OK')
        self.assertEqual(front3('Chocolate') , 'ChoChoCho', 'OK')
        self.assertEqual(front3('abc') , 'abcabcabc', 'OK')

if __name__ == '__main__':
    unittest.main()
