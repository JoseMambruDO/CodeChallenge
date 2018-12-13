#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """
"""Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php"""

from math import *


def q1_twinkle():
    '''1. Write a Python program to print the following string in a specific
    format (see the output). Go to the editor Sample String : "Twinkle, twinkle,
    little star, How I wonder what you are! Up above the world so high, Like a
     diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
     Output :

    Twinkle, twinkle, little star,
    	How I wonder what you are!
    		Up above the world so high,
    		Like a diamond in the sky.
    Twinkle, twinkle, little star,
    	How I wonder what you are
    '''
    string = 'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are'

    # print(string)

    return string


import platform as platf


def q2_python_version():
    '''Write a Python program to get the Python version you are using.'''
    current_version = platf.version()
    return current_version


import datetime


def q3_diplayCurrentDate():
    '''Write a Python program to display the current date and time.'''
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return currentDate


from math import pi


def q4_circleArea(r):
    ''' Write a Python program which accepts the radius of a circle from the
    user and compute the area.'''
    return (r * r) * pi


def q5_circleArea(first, last):
    '''Write a Python program which accepts the user's first and last name
    and print them in reverse order with a space between them. '''
    return '{ } { }'.format(last, first)


def q7_displayExtension(filename):
    '''. Write a Python program to accept a filename from the user and
    print the extension of that.
    Sample filename : abc.java
    Output : java '''
    sp = filename.split('.')
    if (len(sp) > 1):
        return sp[-1]
    return ''


def q6_separe2LT(sep):
    ''' Write a Python program which accepts a sequence of comma-separated
    numbers from user and generate a list and a tuple with those numbers.'''
    l = sep.split(',')
    t = tuple(l)
    return l, t


def q8_firstLastColor():
    '''Write a Python program to display the first and last colors from the
    following list. color_list = ["Red","Green","White" ,"Black"]'''
    color_list = ["Red", "Green", "White", "Black"]
    return color_list[0], color_list[-1]


def q9_examination_date():
    '''Write a Python program to display the examination schedule. (extract the
    date from exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014'''
    exam_st_date = (11, 12, 2014)
    return 'The examination will start from : {0} / {1} / {2}'.format(exam_st_date[0], exam_st_date[1], exam_st_date[2])


def q10_pyramidN(n):
    '''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn'''
    return n + (n * n) + (n * n * n)


def q11_documentsBuiltinF(func):
    '''Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
    Sample function : abs()
    Expected Result :
    abs(number) -> number
    Return the absolute value of the argument.
    '''
    desc = ''
    try:
        f = eval(func)
        desc = f.__doc__
    except NameError as e:
        print('asf')

    return desc


import calendar


def q12_getMonthYear(y, m):
    '''Get month and year in calendar format.'''
    cal = ''
    for d_a in calendar.day_abbr:
        cal += d_a + ' '
    cal += '\n'

    for w in calendar.Calendar().monthdayscalendar(y, m):
        for d in w:
            std = d
            if d == 0:
                std = ''

            cal += '{:>3} '.format(std)
        cal += '\n'

    return cal


def q13_escapeString():
    return """
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
"""


import datetime


def q14_daysBetween(td2, td1):
    '''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days '''
    y, m, d = td2
    d2 = datetime.date(y, m, d)
    y, m, d = td1
    d1 = datetime.date(y, m, d)
    delta = d2 - d1
    return delta.days


def q15_getVolumeSphere(radius):
    '''Write a Python program to get the volume of a sphere with radius 6.'''
    vol = (4 / 3) * pi * pow(radius, 3)
    return round(vol, 2)


def q17_near_oneOrTwoThounsand(num):
    '''Write a Python program to test whether a number is
     within 100 of 1000 or 2000.'''
    return (abs(1000 - num) <= 100) or (abs(2000 - num) <= 100)


def q18_sumOfValues(a, b, c):
    '''Write a Python program to calculate the sum of three given numbers, if
    the values are equal then return thrice of their sum. '''
    l = [a, b, c]
    res = sum(l)
    if (len(set(l)) == 1):
        res *= 3
    return res


def q19_startWithOrAdd(start, word):
    '''Write a Python program to get a new string from a given string where
    "Is" has been added to the front. If the given string already begins with
    "Is" then return the string unchanged. '''

    return word.startswith(star)

def q20_nCopyString(str, n):
    '''Write a Python program to get a string which is n (non-negative integer)
    copies of a given string.'''
    return str * n

def q21_descriEvenOdd(num):
    '''Write a Python program to find whether a given number (accept from the
    user) is even or odd, print out an appropriate message to the user.'''
    msg=str(num) + ' is '
    if num % 2 == 0:
        msg += 'EVEN'
    else:
        msg += 'ODD'
    return msg

def q22_count4(nums):
    '''Write a Python program to count the number 4 in a given list.'''
    return nums.count(4)

def q23_getfirst2Ch(str):
    '''Write a Python program to get the n (non-negative integer) copies of
    the first 2 characters of a given string. Return the n copies of the
    whole string if the length is less than 2'''
    res=''
    if len(str) <= 2:
        res=str
    else:
        res=str[0:2]
    return res

def q24_isVowel(l):
    '''Write a Python program to test
    whether a passed letter is a vowel or not.'''
    vowel = 'aeiou'
    l = l.lower()
    res = False
    if (l in vowel) and l != '':
        res = True
    return res




if __name__ == '__main__':
    print("Some test")
