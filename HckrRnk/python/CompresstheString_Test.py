#!/user/bin/env python
#-*- coding: utf-8 -*-

import unittest
from CompresstheString import *

class CompresstheString_Test(unittest.TestCase):

    def test_CompressTheString(self):

        cts = CompresstheString()
        self.assertEqual(cts.giveCompress('aaaasdfsss'),"(4, a) (1, s) (1, d) (1, f) (3, s)")
        self.assertEqual(cts.giveCompress('1222311'),"(1, 1) (3, 2) (1, 3) (2, 1)")


if __name__=='__main__':
    unittest.main()