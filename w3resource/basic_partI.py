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

    #print(string)

    return string

import platform as platf

def q2_python_version():
    '''2. Write a Python program to get the Python version you are using.'''
    current_version = platf.version()
    return current_version

from math import pi

def q3_circleArea(r):
    return (r*r) * pi

if __name__ == '__main__':
    print('some test')
