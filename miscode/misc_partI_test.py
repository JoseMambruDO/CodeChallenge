#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from misc_partI import *

import re



#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """
"""Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php"""


import unittest
from misc_partI import *

import re

class Misc_Part_Test(unittest.TestCase):

    def test_hasConsecutive(self):
        
        self.assertEqual(hasConsecutive([1,2,3,4]),True)
        self.assertEqual(hasConsecutive([42,21,31,41]),True)
        self.assertEqual(hasConsecutive([30,1,6,8,31]),True)

        self.assertEqual(hasConsecutive([0,0,0,2,4]),False)
        self.assertEqual(hasConsecutive([33,3,3,3,3]),False)
        self.assertEqual(hasConsecutive([5,5,5,5,8]),False)

if __name__ == '__main__':
    unittest.main()
