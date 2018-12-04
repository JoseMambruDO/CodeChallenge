#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """

import unittest
from cb_code_practice import *


class CBCodePractice(unittest.TestCase):

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
        self.assertEqual(missing_char('kitten', 1), 'ktten')
        self.assertEqual(missing_char('kitten', 0), 'itten')
        self.assertEqual(missing_char('kitten', 4), 'kittn')

    def test_from_back(self):
        self.assertEqual(front_back('code'), 'eodc')
        self.assertEqual(front_back('a'), 'a')
        self.assertEqual(front_back('ab'), 'ba')

    def test_front3(self):
        self.assertEqual(front3('Java'), 'JavJavJav', 'OK')
        self.assertEqual(front3('Chocolate'), 'ChoChoCho', 'OK')
        self.assertEqual(front3('abc'), 'abcabcabc', 'OK')

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

    def test_without_end(self):
        self.assertEqual(without_end('Hello'), 'ell')
        self.assertEqual(without_end('java'), 'av')
        self.assertEqual(without_end('coding'), 'odin')

    def test_combo_string(self):
        self.assertEqual(combo_string('Hello', 'hi'), 'hiHellohi')
        self.assertEqual(combo_string('hi', 'Hello'), 'hiHellohi')
        self.assertEqual(combo_string('aaa', 'b'), 'baaab')

    def test_non_start(self):
        self.assertEqual(non_start('Hello', 'There'), 'ellohere')
        self.assertEqual(non_start('java', 'code'), 'avaode')
        self.assertEqual(non_start('shotl', 'java'), 'hotlava')

    def test_left2(self):
        self.assertEqual(left2('Hello'), 'lloHe')
        self.assertEqual(left2('java'), 'vaja')
        self.assertEqual(left2('Hi'), 'Hi')

    def test_first_last6(self):
        self.assertEqual(first_last6([1, 2, 6]), True)
        self.assertEqual(first_last6([6, 1, 2, 3]), True)
        self.assertEqual(first_last6([13, 6, 1, 2, 3]), False)

    def test_same_first_last(self):
        self.assertEqual(same_first_last([1, 2, 3]), False)
        self.assertEqual(same_first_last([1, 2, 3, 1]), True)
        self.assertEqual(same_first_last([1, 2, 1]), True)

    def test_make_pi(self):
        list_make_pi = make_pi()
        self.assertEqual(len(make_pi()), 3)
        self.assertEqual(list_make_pi[0], 3)
        self.assertEqual(list_make_pi[1], 1)
        self.assertEqual(list_make_pi[2], 4)

    def test_common_end(self):
        self.assertEqual(common_end([1, 2, 3], [7, 3]), True)
        self.assertEqual(common_end([1, 2, 3], [7, 3, 2]), False)
        self.assertEqual(common_end([1, 2, 3], [1, 3]),  True)

    def test_sum3(self):
        self.assertEqual(sum3([1, 2, 3]), 6)
        self.assertEqual(sum3([5, 11, 2]), 18)
        self.assertEqual(sum3([7, 0, 0]), 7)

    def test_rotate_left3(self):
        self.assertEqual(rotate_left3([1, 2, 3]), [2, 3, 1])
        self.assertEqual(rotate_left3([5, 11, 9]), [11, 9, 5])
        self.assertEqual(rotate_left3([7, 0, 0]), [0, 0, 7])

    def test_reverse3(self):
        self.assertEqual(reverse3([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse3([5, 11, 9]), [9, 11, 5])
        self.assertEqual(reverse3([7, 0, 0]), [0, 0, 7])

    def test_max_end3(self):
        self.assertEqual(max_end3([1, 2, 3]),  [3, 3, 3])
        self.assertEqual(max_end3([11, 5, 9]),  [11, 11, 11])
        self.assertEqual(max_end3([2, 11, 3]),  [3, 3, 3])

    def test_sums2(self):
        self.assertEqual(sum2([1, 2, 3]), 3)
        self.assertEqual(sum2([1, 1]), 2)
        self.assertEqual(sum2([1, 1, 1, 1]), 2)

    def test_middle_way(self):
        self.assertEqual(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
        self.assertEqual(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
        self.assertEqual(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])

    def test_make_ends(self):
        self.assertEqual(make_ends([1, 2, 3]), [1, 3])
        self.assertEqual(make_ends([1, 2, 3, 4]), [1, 4])
        self.assertEqual(make_ends([7, 4, 6, 2]), [7, 2])

    def test_has23(self):
        self.assertEqual(has23([2, 5]), True)
        self.assertEqual(has23([4, 3]), True)
        self.assertEqual(has23([4, 5]), False)

    def test_cigar_party(self):
        self.assertEqual(cigar_party(30, False), False)
        self.assertEqual(cigar_party(50, False), True)
        self.assertEqual(cigar_party(70, True), True)

    def test_date_fashion(self):
        self.assertEqual(date_fashion(5, 10), 2)
        self.assertEqual(date_fashion(5, 2), 0)
        self.assertEqual(date_fashion(5, 5), 1)

    def test_squirrel_play(self):
        self.assertEqual(squirrel_play(70, False), True)
        self.assertEqual(squirrel_play(95, False), False)
        self.assertEqual(squirrel_play(95, True), True)

    def test_caught_speeding(self):
        self.assertEqual(caught_speeding(60, False), 0)
        self.assertEqual(caught_speeding(65, False), 1)
        self.assertEqual(caught_speeding(65, True), 0)

    def test_sorta_sum(self):
        self.assertEqual(sorta_sum(3, 4), 7)
        self.assertEqual(sorta_sum(9, 4), 20)
        self.assertEqual(sorta_sum(10, 11), 21)

    def test_alarm_clock(self):
        self.assertEqual(alarm_clock(1, False), '7:00')
        self.assertEqual(alarm_clock(5, False), '7:00')
        self.assertEqual(alarm_clock(0, False), '10:00')

    def test_love6(self):
        self.assertEqual(love6(6, 4), True)
        self.assertEqual(love6(4, 5), False)
        self.assertEqual(love6(1, 5), True)

    def test_in1to10(self):
        self.assertEqual(in1to10(5, False), True)
        self.assertEqual(in1to10(11, False), False)
        self.assertEqual(in1to10(11, True), True)

    def test_near_ten(self):
        self.assertEqual(near_ten(12), True)
        self.assertEqual(near_ten(17), False)
        self.assertEqual(near_ten(19), True)

    # Test Logic-2
    def test_make_bricks(self):
        self.assertEqual(make_bricks(3, 1, 8), True)
        self.assertEqual(make_bricks(3, 1, 9), False)
        self.assertEqual(make_bricks(3, 2, 10), True)

    def test_lone_sum(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)
        self.assertEqual(lone_sum(3, 2, 3), 2)
        self.assertEqual(lone_sum(3, 3, 3), 0)

    def test_lucky_sum(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)
        self.assertEqual(lucky_sum(1, 2, 13), 3)
        self.assertEqual(lucky_sum(1, 13, 3), 1)

    def test_no_teen_sum(self):
        self.assertEqual(no_teen_sum(1, 2, 3) , 6)
        self.assertEqual(no_teen_sum(2, 13, 1) , 3)
        self.assertEqual(no_teen_sum(2, 1, 14) , 3)

    def test_close_far(self):
        self.assertEqual(close_far(1, 2, 10) , True)
        self.assertEqual(close_far(1, 2, 3) , False)
        self.assertEqual(close_far(4, 1, 3) , True)

    def test_make_chocolate(self):
        self.assertEqual(make_chocolate(4, 1, 9) , 4)
        self.assertEqual(make_chocolate(4, 1, 10) , -1)
        self.assertEqual(make_chocolate(4, 1, 7) , 2)

    #String-2
    def test_double_char(self):
        self.assertEqual(double_char('The') , 'TThhee')
        self.assertEqual(double_char('AAbb') , 'AAAAbbbb')
        self.assertEqual(double_char('Hi-There') , 'HHii--TThheerree')

    def test_count_hi(self):
        self.assertEqual(count_hi('abc hi ho') , 1)
        self.assertEqual(count_hi('ABChi hi') , 2)
        self.assertEqual(count_hi('hihi') , 2)

    def test_cat_dog(self):
        self.assertEqual(cat_dog('catdog') , True)
        self.assertEqual(cat_dog('catcat') , False)
        self.assertEqual(cat_dog('1cat1cadodog')  True)

    def test_count_code(self):
        self.assertEqual(count_code('aaacodebbb') , 1)
        self.assertEqual(count_code('codexxcode') , 2)
        self.assertEqual(count_code('cozexxcope') , 2)

    def test_end_other(self):
        self.assertEqual(end_other('Hiabc', 'abc')  , True)
        self.assertEqual(end_other('AbC', 'HiaBc')  , True)
        self.assertEqual(end_other('abc', 'abXabc') , True)

    def test_xyz_there(self):
        self.assertEqual(xyz_there('abcxyz') , True)
        self.assertEqual(xyz_there('abc.xyz') , False)
        self.assertEqual(xyz_there('xyz.abc') , True)

    def test_count_evens(self):
        self.assertEqual(count_evens([2, 1, 2, 3, 4]) , 3)
        self.assertEqual(count_evens([2, 2, 0]) , 3)
        self.assertEqual(count_evens([1, 3, 5]) , 0)

    def test_big_diff(self):
        self.assertEqual(big_diff([10, 3, 5, 6]) , 7)
        self.assertEqual(big_diff([7, 2, 10, 9]) , 8)
        self.assertEqual(big_diff([2, 10, 7, 2]) , 8)

    def test_centered_average(self):
        self.assertEqual(centered_average([1, 2, 3, 4, 100]) , 3)
        self.assertEqual(centered_average([1, 1, 5, 5, 10, 8, 7]) , 5)
        self.assertEqual(centered_average([-10, -4, -2, -4, -2, 0]) , -3)

    def test_centered_average(self):
        self.assertEqual(sum13([1, 2, 2, 1]) , 6)
        self.assertEqual(sum13([1, 1]) , 2)
        self.assertEqual(sum13([1, 2, 2, 1, 13]) , 6)


if __name__ == '__main__':
    unittest.main()
