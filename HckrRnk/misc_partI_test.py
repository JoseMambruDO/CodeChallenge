#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from misc_partI import *

import re

class Misc_Part_Test(unittest.TestCase):

    def test_averageDiff(self):
        
        self.assertEqual(averageDiff([154,161,167,170,171,174,176,182]),169.375)

    def test_veriPolinomial(self):

        self.assertEqual(verifyPolinomial("1 4","x**3 + x**2 + x + 1"),True)


if __name__ == '__main__':
    unittest.main()
