#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from misc_partI import *

import re

class Misc_Part_Test(unittest.TestCase):

    def _test_averageDiff(self):
        
        self.assertEqual(averageDiff([154,161,167,170,171,174,176,182]),169.375)

    def _test_veriPolinomial(self):

        self.assertEqual(verifyPolinomial("1 4","x**3 + x**2 + x + 1"),True)

    def test_veriPolinomial(self):
        self.assertEqual(valid("B1CDEF2354"),True)
        self.assertEqual(valid("BCCDEF2E54"),False)
        self.assertEqual(valid("B1CBEF2354"),False)
        self.assertEqual(valid("B1CDEF+354"),False)


if __name__ == '__main__':
    unittest.main()
