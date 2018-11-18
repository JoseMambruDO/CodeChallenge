#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """

import unittest
from warmup2 import *


class Warmup2Tests(unittest.TestCase):

    def test_string_times(self):
        self.assertEqual(string_times('Hi', 2), 'HiHi')
        self.assertEqual(string_times('Hi', 3), 'HiHiHi')
        self.assertEqual(string_times('Hi', 1), 'Hi')

    def test_front_times(self):
        self.assertEqual(front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(front_times('Abc', 3), 'AbcAbcAbc')

    def test_string_bits(self):
        self.assertEqual(string_bits('Hello'), 'Hlo')
        self.assertEqual(string_bits('Hi'), 'H')
        self.assertEqual(string_bits('Heeololeo'), 'Hello')

    def test_string_splosion(self):
        self.assertEqual(string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(string_splosion('abc'), 'aababc')
        self.assertEqual(string_splosion('ab'), 'aab')

    def test_last2(self):
        self.assertEqual(last2('hixxhi'), 1)
        self.assertEqual(last2('xaxxaxaxx'), 1)
        self.assertEqual(last2('axxxaaxx'), 2)


if __name__ == '__main__':
    unittest.main()
