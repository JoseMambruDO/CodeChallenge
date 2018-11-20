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

    def test_array_count9(self):
        self.assertEqual(array_count9([1, 2, 9]), 1)
        self.assertEqual(array_count9([1, 9, 9]), 2)
        self.assertEqual(array_count9([1, 9, 9, 3, 9]), 3)

    def test_array_front9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)

    def test_array123(self):
        self.assertEqual(array123([1, 1, 2, 3, 1]), True)
        self.assertEqual(array123([1, 1, 2, 4, 1]), False)
        self.assertEqual(array123([1, 1, 2, 1, 2, 3]), True)

    def test_string_match(self):
        self.assertEqual(string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(string_match('abc', 'abc'), 2)
        self.assertEqual(string_match('abc', 'axc'), 0)

    def test_hello_name(self):
        self.assertEqual(hello_name('Bob'), 'Hello Bob!')
        self.assertEqual(hello_name('Alice'), 'Hello Alice!')
        self.assertEqual(hello_name('X'), 'Hello X!')

    def test_make_abba(self):
        self.assertEqual(make_abba('Hi', 'Bye'), 'HiByeByeHi')
        self.assertEqual(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
        self.assertEqual(make_abba('What', 'Up'), 'WhatUpUpWhat')

    def test_make_tags(self):
        self.assertEqual(make_tags('i', 'Yay'), '<i>Yay</i>')
        self.assertEqual(make_tags('i', 'Hello'), '<i>Hello</i>')
        self.assertEqual(make_tags('cite', 'Yay'), '<cite>Yay</cite>')

    def test_make_out_word(self):
        self.assertEqual(make_out_word('<<>>', 'Yay'), '<<Yay>>')
        self.assertEqual(make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
        self.assertEqual(make_out_word('[[]]', 'word'), '[[word]]')

    def test_extra_end(self):
        self.assertEqual(extra_end('Hello'), 'lololo')
        self.assertEqual(extra_end('ab'), 'ababab')
        self.assertEqual(extra_end('Hi'), 'HiHiHi')

    def test_extra_end(self):
        self.assertEqual(extra_end('Hello'), 'lololo')
        self.assertEqual(extra_end('ab'), 'ababab')
        self.assertEqual(extra_end('Hi'), 'HiHiHi')

    def test_first_two(self):
        self.assertEqual(first_two('Hello'), 'He')
        self.assertEqual(first_two('abcdefg'), 'ab')
        self.assertEqual(first_two('ab'), 'ab')

    def test_first_half(self):
        self.assertEqual(first_half('WooHoo'), 'Woo')
        self.assertEqual(first_half('HelloThere'), 'Hello')
        self.assertEqual(first_half('abcdef'), 'abc')


if __name__ == '__main__':
    unittest.main()
