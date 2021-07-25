#!/user/bin/env python
#-*- coding: utf-8 -*-

import unittest
from IterablesAndIterators import *

class IterablesAndIterators_Test(unittest.TestCase):

    def test_IterablesAndIterators(self):

        iai = IterablesAndIterators()
        self.assertEqual(iai.propablity_e_in_elements('a a c d',2,'a'),0.8333)


if __name__=='__main__':
    unittest.main()