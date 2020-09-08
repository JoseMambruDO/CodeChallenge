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
        self.assertEqual(hasConsecutive([11,21,31,41]),False)
        self.assertEqual(hasConsecutive([0,1,6,8]),True)
        self.assertEqual(hasConsecutive([0,0,0,0]),False)
        self.assertEqual(hasConsecutive([4,4,5,0]),False)
        self.assertEqual(hasConsecutive([0,0,6,7]),False)

if __name__ == '__main__':
    unittest.main()
