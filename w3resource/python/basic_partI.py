#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Some wonderful lines in python """
"""Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php"""

from math import *


def q1_twinkle():
    '''1. Write a Python program to print the following string in a specific
    format (see the output). Sample String : "Twinkle, twinkle,
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


def q5_reverseFirstLast(first, last):
    '''Write a Python program which accepts the user's first and last name
    and print them in reverse order with a space between them. '''
    return '{ } { }'.format(last, first)

def q6_separe2LT(sep):
    ''' Write a Python program which accepts a sequence of comma-separated
    numbers from user and generate a list and a tuple with those numbers.'''
    l = sep.split(',')
    t = tuple(l)
    return l, t


def q7_displayExtension(filename):
    '''. Write a Python program to accept a filename from the user and
    print the extension of that.
    Sample filename : abc.java
    Output : java '''
    sp = filename.split('.')
    if (len(sp) > 1):
        return sp[-1]
    return ''

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
        pass

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

    return word.startswith(start)


def q20_nCopyString(str, n):
    '''Write a Python program to get a string which is n (non-negative integer)
    copies of a given string.'''
    return str * n


def q21_descriEvenOdd(num):
    '''Write a Python program to find whether a given number (accept from the
    user) is even or odd, print out an appropriate message to the user.'''
    msg = str(num) + ' is '
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
    res = ''
    if len(str) <= 2:
        res = str
    else:
        res = str[0:2]
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


def q25_eInGroup(e, g):
    '''Write a Python program to check whether a specified value is
    contained in a group of values.'''
    return e in g


def q26_AscHistogram(nums):
    '''Write a Python program to create a histogram from a given list
    of integers.'''

    ch = '@'
    res = ''
    for i in nums:
        res += ch * i
        res += '\n'
    return res


def q27_concatenateAllElements(li):
    '''Write a Python program to concatenate all elements in a list into
    a string and return it.'''
    list_str = list(map(str, li))
    return ''.join(list_str)


def q28_numsBeforE(nums, E):
    '''Write a Python program to print all even numbers from a given numbers
    list in the same order and stop the printing if any numbers that come
    after 237 in the sequence.'''
    i = nums.index(E)
    return nums[0: i]


def q29_getUniqMemberSet(s1, s2):
    '''Write a Python program to print out a set containing all the colors from
    a list which are not present in another list '''
    un = [i for i in s1 if i not in s2]
    return un


def q30_getTriangleArea(b, h):
    '''Write a Python program that will accept the base and
    height of a triangle and compute the area'''
    return 0.5 * b * h


def q31_getGCD(x, y):
    '''Write a Python program to compute the greatest common
    divisor (GCD) of two positive integers.'''
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


def q32_getLCM(x, y):
    '''32. Write a Python program to get the least common multiple
    (LCM) of two positive integers'''
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm


def q33_sumThreeInteger(a, b, c):
    '''33. Write a Python program to sum of three given integers. However, if two
    values are equal sum will be zero.'''
    re = 0
    nums = [a, b, c]
    fnums = [i for i in nums if nums.count(i) == 1]
    if len(fnums) == 3:
        re = sum(fnums)
    return re


def q34_sumTwoIntegers20(a, b):
    '''34. Write a Python program to sum of two given integers. However, if the sum
    is between 15 to 20 it will return 20.'''
    re = a + b
    if re >= 15 and re <= 20:
        re = 20
    return re


def q35_twoSumDiff5(a, b):
    '''35. Write a Python program that will return true if the two given integer
    values are equal or their sum or difference is 5.'''
    re = False
    if ((a == b) or (a + b == 5) or (abs(a - b) == 5)):
        re = True
    return re


def q36_sumIntegers(a, b):
    '''36. Write a Python program to add two objects if both objects are an integer
    type.'''
    re = 0
    if (type(a) is int) and (type(b) is int):
        re = a + b
    return re


def q37_infoContact(name, age, address):
    '''37. Write a Python program to display your details like name, age, address in
    three different lines.'''
    return 'Name: {}\nAge: {}\n address{}\n'.format(name, age, address)


def q38_solveEq(x, y):
    '''38. Write a Python program to solve (x + y) * (x + y).
    Test Data : x = 4, y = 3
    Expected Output : (4 + 3) ^ 2) = 49'''
    return (x + y) * (x + y)


def q39_mortage(amt, int, years):
    '''39. Write a Python program to compute the future value of a specified principal
    amount, rate of interest, and a number of years.
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79'''
    return amt * (3.5 ** 7)


from math import sqrt

def q40_distBetweenPoints(x1, y1, x2, y2):
    '''40. Write a Python program to compute the distance between
    the points (x1, y1) and (x2, y2).'''
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


from os import stat

def q41_checkExistsFile(pFile):
    '''41. Write a Python program to check whether a file exists.'''
    re = False
    try:
        st = stat(pFile)
        re = True
    except FileNotFoundError:
        print('this file not exists.')

    return re


import platform


def q42_archOS():
    '''42. Write a Python program to determine if a Python shell is executing in
    32bit or 64bit mode on OS.'''
    is_64bits = sys.maxsize > 2**32
    re = 'bit'
    if is_64bits:
        re = '64' + re
    else:
        re = '32' + re
    return re


import platform as p


def q43_OSInfo():
    '''43. Write a Python program to get OS name, platform
    and release information.'''
    return 'OS name: {}\nplaform: {}\n release information{}\n'.format(p.system(), p.version(), p.release())


import site as s


def q44_PythonSitePackages():
    '''44. Write a Python program to locate Python site-packages.'''
    sitepackages = s.getsitepackages()
    return sitepackages


from os import system


def q45_executeCommand(command):
    '''45. Write a python program to call an external command in Python.'''
    system(command)


import os


def q46_pathNName():
    '''46. Write a python program to get the path and name of the file that
    is currently executing.'''
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return 'dirname:{}\n file:{}\n'.format(dirname, filename)


from os import cpu_count


def q47_getNumberCPUs():
    '''47. Write a Python program to find out the number of CPUs using.'''
    return cpu_count()


def q48_str2Number(value):
    '''48. Write a Python program to parse a string to Float or Integer.'''
    re = None
    if value.isnumeric():
        if value.isdecimal():
            re = float(value)
        else:
            re = int(value)
    return re


from os import listdir


def q49_dirAllFiles(dir):
    '''49. Write a Python program to list all files in a directory in Python.'''
    return (listdir(dir))


def q50_dropNewLineorSpace(value):
    '''50. Write a Python program to print without newline or space.'''
    re = value.replace(' ', '').replace('\n', '')
    return re


import cProfile


def q51_profilePyProgram(expresion):
    '''51. Write a Python program to determine profiling of Python programs.
    Note: A profile is a set of statistics that describes how often and for
    how long various parts of the program executed. These statistics can be
    formatted into reports via the pstats module.
    '''
    cProfile.run(expresion)


import sys


def q52_writeStderr(err):
    '''52. Write a Python program to print to stderr.'''
    sys.stderr.write(err)


from os import environ


def q53_accessEnvVar(var):
    '''53. Write a python program to access environment variables.'''
    res = ''
    try:
        res = os.environ[var]
    except KeyError:
        print ("KeyError, use other variable")
    return res

from os import getlogin
def q54_getCurrentUsername():
    '''54. Write a Python program to get the current username'''
    return getlogin()

from socket import gethostbyname, gethostname

def q55_getLocalIPAddresses():
    '''55. Write a Python to find local IP addresses using Python's stdlib'''
    return gethostbyname(gethostname())

import fcntl, termios, struct
def q56_getHeightAndWidthConsole():
    '''56. Write a Python program to get height and width of the console window.'''
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th


'''57. Write a program to get execution time for a Python method.'''

def q58_sumFirstNPositiveInts(nums):
    '''58. Write a python program to sum of the first n positive integers.'''
    positive = [i for i in nums if i>0]
    return sum(positive)

def q59_convertHeightfi2c(f,i):
    '''59. Write a Python program to convert height (in feet and inches)
    to centimeters.'''
    return (f*30.48)+(i*2.54)

def q60_calculateHyp(a,b):
    '''60. Write a Python program to calculate the hypotenuse of
    a right angled triangle.'''
    return sqrt(a**2 + b**2)

def q61_convertDistancef2iym(f):
    '''61. Write a Python program to convert the distance (in feet) to inches,
    yards, and miles.'''
    i=f*12
    y=f/3
    m=f*39.37
    return i,y,m

def q62_convertTimetoSeconds(days,hours, minutes, seconds):
    '''62. Write a Python program to convert all units of time into seconds.'''
    time = (days * 3600 * 24) + (hours *3600) + (minutes*60)+seconds
    return time

def q63_getAbsPathFile(file):
    '''63. Write a Python program to get an absolute file path.'''
    return os.path.abspath(file)

import time
def q64_getFileCreationModification(file):
    '''64. Write a Python program to get file creation and modification
    date/times.'''
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    return time.ctime(mtime), time.ctime(mtime)

def q65_converSecondsToDHM(time):
    '''65. Write a Python program to convert seconds to day, hour,
    minutes and seconds.'''
    d = time // (24 * 3600)
    time = time % (24 * 3600)
    h = time // 3600
    time %= 3600
    m = time // 60
    time %= 60
    s = time
    return d,h,m,s

def q66_calculateBMI(w,h):
    '''66. Write a Python program to calculate body mass index.'''
    return w /(h*h)

def q67_convertPressure(kpa):
    '''67. Write a Python program to convert pressure in kilopascals to pounds
    per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.'''
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325
    return (psi, mmhg, atm)

def q68_sumDigitsString(value):
    '''68. Write a Python program to calculate the sum of the digits
    in an integer.'''
    res = 0
    for i in value:
        res += int(i)
    return res
def q69_sortThreeIntegers(a,b,c):
    '''69. Write a Python program to sort three integers without using conditional
    statements and loops.'''
    l = [a,b,c]
    return sorted(l)

import glob
import os
def q70_sortFilesByDate(ext):
    '''70. Write a Python program to sort files by date.'''
    files = glob.glob(ext)
    files.sort(key=os.path.getmtime)
    return ("\n".join(files))

import glob
import os
def q71_sortFilesByCreationDate(ext):
    '''71. Write a Python program to get a directory listing, sorted by creation date.'''
    files = glob.glob(ext)
    files.sort(key=os.path.getctime)
    return ("\n".join(files))

import math
def q72_getDetailsMathModule():
    '''72. Write a Python program to get the details of math module.'''

    return dir(math)


#
#
# TODO LIST
#

'''73. Write a Python program to calculate midpoints of a line.'''


'''74. Write a Python program to hash a word.'''


'''75. Write a Python program to get the copyright information.'''


'''76. Write a Python program to get the command-line arguments
(name of the script, the number of arguments, arguments) passed to a script.'''


'''77. Write a Python program to test whether the system is a
big-endian platform or little-endian platform.'''


'''78. Write a Python program to find the available built-in modules.'''


'''79. Write a Python program to get the size of an object in bytes.'''


'''80. Write a Python program to get the current value of the recursion limit.'''


'''81. Write a Python program to concatenate N strings.'''


'''82. Write a Python program to calculate the sum over a container.'''


'''83. Write a Python program to test whether all numbers of a list is greater
than a certain number.'''


'''84. Write a Python program to count the number occurrence of a specific
character in a string.'''


'''85. Write a Python program to check if a file path is a file or a directory.'''


'''86. Write a Python program to get the ASCII value of a character.'''


'''87. Write a Python program to get the size of a file.'''


'''88. Given variables x=30 and y=20, write a Python program to
print t "30+20=50".'''


'''89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a
Month!" and do nothing if the value is not equal.
'''

'''90. Write a Python program to create a copy of its own source code.'''


'''91. Write a Python program to swap two variables.'''


'''92. Write a Python program to define a string containing special characters
in various forms.'''


'''93. Write a Python program to get the identity of an object.'''


'''94. Write a Python program to convert a byte string to a list of integers.'''


'''95. Write a Python program to check if a string is numeric.'''


'''96. Write a Python program to print the current call stack.'''


'''97. Write a Python program to list the special variables used within the
language.'''


'''98. Write a Python program to get the system time.
Note : The system time is important for debugging, network information,
random number seeds, or something as simple as program performance.
'''

'''99. Write a Python program to clear the screen or terminal.'''


'''100. Write a Python program to get the name of the host on which the routine
is running.'''


'''101. Write a Python program to access and print a URL's content to the
console.'''


'''102. Write a Python program to get system command output.'''


'''103. Write a Python program to extract the filename from a given path.'''


'''104. Write a Python program to get the effective group id, effective user id,
real group id, a list of supplemental group ids associated with the current process.
Note: Availability: Unix.
'''

'''105. Write a Python program to get the users environment.'''


'''106. Write a Python program to divide a path on the extension separator.'''


'''107. Write a Python program to retrieve file properties.'''


'''108. Write a Python program to find path refers to a file or directory when
you encounter a path name.'''


'''109. Write a Python program to check if a number is positive, negative or zero.'''


'''110. Write a Python program to get numbers divisible by fifteen from a list
using an anonymous function.'''


'''111. Write a Python program to make file lists from current directory using
a wildcard.'''


'''112. Write a Python program to remove the first item from a specified list.'''


'''113. Write a Python program to input a number, if it is not a number generate
an error message.'''


'''114. Write a Python program to filter the positive numbers from a list.'''


'''115. Write a Python program to compute the product of a list of integers
(without using for loop).'''


'''116. Write a Python program to print Unicode characters.'''


'''117. Write a Python program to prove that two string variables of same value
point same memory location.'''


'''118. Write a Python program to create a bytearray from a list.'''


'''119. Write a Python program to display a floating number in specified
numbers.'''


'''120. Write a Python program to format a specified string to limit the number
of characters to 6.'''


'''121. Write a Python program to determine if variable is defined or not.'''


'''122. Write a Python program to empty a variable without destroying it.

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}
'''


'''123. Write a Python program to determine the largest and smallest integers,
longs, floats.'''


'''124. Write a Python program to check if multiple variables
have the same value.'''


'''125. Write a Python program to sum of all counts in a collections?'''


'''126. Write a Python program to get the actual module object for a
given object.'''


'''127. Write a Python program to check if an integer fits in 64 bits.'''


'''128. Write a Python program to check if lowercase letters exist in a
string.'''


'''129. Write a Python program to add leading zeroes to a string.'''


'''130. Write a Python program to use double quotes to display strings.'''


'''131. Write a Python program to split a variable length string into variables.'''


'''132. Write a Python program to list home directory without absolute path.'''


'''133. Write a Python program to calculate the time runs (difference between
start and current time) of a program.'''


'''134. Write a Python program to input two integers in a single line.'''


'''135. Write a Python program to print a variable without spaces between values.
Sample value : x =30
Expected output : Value of x is "30"
'''

'''136. Write a Python program to find files and skip directories of a
given directory.'''


'''137. Write a Python program to extract single key-value pair of a
dictionary in variables.'''


'''138. Write a Python program to convert true to 1 and false to 0.'''


'''139. Write a Python program to valid a IP address.'''


'''140. Write a Python program to convert an integer to binary keep
leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100
'''

'''141. Write a python program to convert decimal
to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04
'''

'''142. Write a Python program to find the operating system name, platform and
platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic'''


'''143. Write a Python program to determine if the python shell is executing in
32bit or 64bit mode on operating system.'''


'''144. Write a Python program to check if variable is of integer or string.'''


'''145. Write a Python program to find the operating system name,
platform and platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic'''


'''146. Write a Python program to find the location of Python module sources.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic'''


'''147. Write a Python function to check whether a number is divisible by
another number. Accept two integers values form the user.'''


'''148. Write a Python function to find the maximum and minimum numbers from a
sequence of numbers.
Note: Do not use built-in functions.
'''

'''149. Write a Python function that takes a positive integer and returns the
sum of the cube of all the positive integers smaller than the specified number.'''


'''150. Write a Python function to find a distinct pair of numbers whose product
is odd from a sequence of integer values.'''
