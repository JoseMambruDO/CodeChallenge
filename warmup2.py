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
