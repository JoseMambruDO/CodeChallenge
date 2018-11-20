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
