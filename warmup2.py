#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """


def string_times(str, n):
    '''Given a string and a non-negative int n, return a larger string that is n copies of the original string.'''
    return str * n


def front_times(str, n):
    ''' Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
     or whatever is there if the string is less than length 3. Return n copies of the front;'''
    r = ''
    if len(str) < 3:
        r = n * str
    else:
        r = n * str[0:3]

    return r


def string_bits(str):
    ''' Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". '''
    l = [str[i] for i in range(0, len(str)) if i % 2 == 0]
    return "".join(l)


def string_splosion(str):
    '''Given a non-empty string like "Code" return a string like "CCoCodCode".'''
    lstr = [str[:i + 1] for i in range(len(str))]
    return "".join(lstr)


def last2(str):
    '''Given a string, return the count of the number of times that a substring
    length 2 appears in the string and also as the last 2 chars of the string,
    so "hixxxhi" yields 1 (we won't count the end substring).'''
    app_num = 0
    len_str = len(str)
    if len_str < 2:
        return app_num
    l2 = str[len_str - 2:]
    for i in range(len_str - 2):
        sub = str[i:i + 2]
        if sub == l2:
            app_num += 1
    return app_num


def array_count9(nums):
    '''Given an array of ints, return the number of 9's in the array.'''
    count9 = 0
    for i in nums:
        count9 += 1 if i == 9 else 0
    return count9


def array_front9(nums):
    '''Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.'''
    return 9 in nums[:4]


def array123(nums):
    '''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.'''
    result = False
    for i in range(len(nums)):
        if nums[i:i + 3] == [1, 2, 3]:
            result = True
    return result


def string_match(a, b):
    '''Given 2 strings, a and b, return the number of the positions where they contain
    the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in both strings.'''
    list_a = [a[i:i + 2] for i in range(len(a) - 1)]
    list_b = [b[i:i + 2] for i in range(len(b) - 1)]
    count_match = 0
    for la in set(list_a):
        if (la in set(list_b)):
            count_match += 1
    return count_match


def hello_name(name):
    '''Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".'''

    return 'Hello ' + name + '!'


def make_abba(a, b):
    '''Given two strings, a and b, return the result of putting them together in
    the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".'''

    return a + 2 * b + a


def make_tags(tag, word):
    '''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as
    italic text. In this example, the "i" tag makes <i> and </i> which surround
    the word "Yay". Given tag and word strings, create the HTML string with tags
    around the word, e.g. "<i>Yay</i>".'''

    return "<{0}>{1}<{0}/>".format(tag, word)


def make_out_word(out, word):
    '''Given an "out" string length 4, such as "<<>>", and a word, return a new
    string where the word is in the middle of the out string, e.g. "<<word>>". '''

    len_out = len(out)
    p1 = out[:len_out // 2]
    p2 = out[len_out // 2:]

    return p1 + word + p2


def extra_end(str):
    '''Given a string, return a new string made of 3 copies of the last 2 chars
    of the original string. The string length will be at least 2.'''

    return 3 * str[-2:]


def first_two(str):
    '''Given a string, return the string made of its first two chars, so the
    String "Hello" yields "He". If the string is shorter than length 2, return
    whatever there is, so "X" yields "X", and the empty string "" yields
    the empty string "". '''

    return str[0:2]


def first_half(str):
    '''Given a string of even length, return the first half. So the string "WooHoo"
    yields "Woo".'''

    len_str = len(str)
    return str[:len_str // 2]


def without_end(str):
    '''Given a string, return a version without the first and last char,
    so "Hello" yields "ell". The string length will be at least 2.'''

    return str[1:-1]


def combo_string(a, b):
    '''Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).'''

    if (len(b) > len(a)):
        a, b = b, a
    return b + a + b


def non_start(a, b):
    '''Given 2 strings, return their concatenation, except omit the first char
    of each. The strings will be at least length 1.'''
    return a[1:] + b[1:]


def left2(str):
    '''Given a string, return a "rotated left 2" version where the first 2 chars
    are moved to the end. The string length will be at least 2.'''
    result = str
    if (len(str) > 2):
        result = str[2:] + str[:2]
    return result


def first_last6(nums):
    '''Given an array of ints, return True if 6 appears as either the first or
    last element in the array. The array will be length 1 or more.'''
    return (nums[0] == 6 or nums[-1] == 6)


def same_first_last(nums):
    ''' Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.'''
    return (len(nums) >= 1 and (nums[0] == nums[-n]))


def make_pi():
    '''Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.'''
    pint = str(int(math.pi * 100))
    results = list(map(int, pint))
    return results


def common_end(a, b):
    '''Given 2 arrays of ints, a and b, return True if they have the same first
    element or they have the same last element. Both arrays will be length 1 or more.'''
    return a[1] == b[1] or a[-1] == b[-1]


def sum3(nums):
    '''Given an array of ints length 3, return the sum of all the elements.'''
    return sum(nums)


def rotate_left3(nums):
    '''Given an array of ints length 3, return an array with the elements
     "rotated left" so {1, 2, 3} yields {2, 3, 1}.'''
    first_element = nums[0]
    del nums[0]
    nums = nums + [first_element]
    return nums


def reverse3(nums):
    '''Given an array of ints length 3, return a new array with the elements in
    reverse order, so {1, 2, 3} becomes {3, 2, 1}.'''
    nums.reverse()
    return nums
