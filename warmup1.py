#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """

from math import *

def sleep_in(weekday, vacation):
    ''' The parameter weekday is True if it is a weekday,
    and the parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. '''

    return not weekday or vacation

    # test
    #print("sleep_in(False, False) ? True ---" + str( sleep_in(False, False)))
    #print("sleep_in(True, False) ? False ---" + str( sleep_in(True, False)))
    #print("sleep_in(False, True) ? True  ---" + str( sleep_in(False, True)))


def monkey_trouble(a_smile, b_smile):
    '''We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
       We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.'''
    return a_smile == b_smile

    # test
    #print("monkey_trouble(True, True) ? True ---" + str( monkey_trouble(True, True)))
    #print("monkey_trouble(False, False) ? True ---" + str( monkey_trouble(False, False)))
    #print("monkey_trouble(True, False) ? False ---" + str( monkey_trouble(True, False)))


def sum_double(a, b):
    ''' Given two int values, return their sum. Unless the two values are the same, then return double their sum.
    '''
    r = a + b
    if a == b:
        r = 2 * r
    return r

    # test
    #print("sum_double(1, 2) ? 3 ---" + str( sum_double(1, 2)))
    #print("sum_double(3, 2) ? 5 ---" + str(sum_double(1, 2)))
    #print("sum_double(2, 2) ? 8 ---" + str(sum_double(1, 2)))

def diff21(n):
    '''Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.
    '''
    r = 21 - n
    if (n > 21):
        r *= 2

    return abs(r)

def parrot_trouble(talking, hour):
    '''We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
    We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.'''

    return talking and (hour < 7 or hour > 20)

def makes10(a,b):
    '''Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.'''
    return (a+b == 10 or a == 10 or b == 10)

def near_hundred(n):
    '''Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.'''
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

 
