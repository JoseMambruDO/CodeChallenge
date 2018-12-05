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
    # print("sleep_in(False, False) ? True ---" + str( sleep_in(False, False)))
    # print("sleep_in(True, False) ? False ---" + str( sleep_in(True, False)))
    # print("sleep_in(False, True) ? True  ---" + str( sleep_in(False, True)))


def monkey_trouble(a_smile, b_smile):
    '''We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
       We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.'''
    return a_smile == b_smile

    # test
    # print("monkey_trouble(True, True) ? True ---" + str( monkey_trouble(True, True)))
    # print("monkey_trouble(False, False) ? True ---" + str( monkey_trouble(False, False)))
    # print("monkey_trouble(True, False) ? False ---" + str( monkey_trouble(True, False)))


def sum_double(a, b):
    ''' Given two int values, return their sum. Unless the two values are the same, then return double their sum.
    '''
    r = a + b
    if a == b:
        r = 2 * r
    return r

    # test
    # print("sum_double(1, 2) ? 3 ---" + str( sum_double(1, 2)))
    # print("sum_double(3, 2) ? 5 ---" + str(sum_double(1, 2)))
    # print("sum_double(2, 2) ? 8 ---" + str(sum_double(1, 2)))


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


def makes10(a, b):
    '''Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.'''
    return (a + b == 10 or a == 10 or b == 10)


def near_hundred(n):
    '''Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.'''
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def pos_neg(a, b, negative):
    '''Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.'''
    r = False
    if (negative):
        r = (a < 0 and b < 0)
    else:
        if not (a < 0 and b < 0):
            r = (a < 0 or b < 0)

    return r


def not_string(str):
    '''Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. '''
    if (not str.startswith('not')):
        str = 'not ' + str
    return str


def missing_char(str, n):
    '''Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).'''
    return str[0:n] + str[n + 1:len(str)]


def front_back(str):
    '''Given a string, return a new string where the first and last chars have been exchanged.'''
    if (len(str) > 1):
        str = str[len(str) - 1] + str[1:len(str) - 1] + str[0]
    return str


def front3(str):
    '''Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.'''
    if (len(str) >= 3):
        str = str[0:3] * 3
    else:
        str = str * 3
    return str


def string_times(str, n):
    '''Given a string and a non-negative int n, return a larger string that is n
    copies of the original string.'''
    return str * n


def front_times(str, n):
    ''' Given a string and a non-negative int n, we'll say that the front of the
    string is the first 3 chars, or whatever is there if the string is less than
    length 3. Return n copies of the front;'''
    r = ''
    if len(str) < 3:
        r = n * str
    else:
        r = n * str[0:3]

    return r


def string_bits(str):
    ''' Given a string, return a new string made of every other char starting
    with the first, so "Hello" yields "Hlo". '''
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
    '''Given an array of ints, return True if one of the first 4 elements in the
    array is a 9. The array length may be less than 4.'''
    return 9 in nums[:4]


def array123(nums):
    '''Given an array of ints, return True if the sequence of numbers 1, 2, 3
    appears in the array somewhere.'''
    result = False
    for i in range(len(nums)):
        if nums[i:i + 3] == [1, 2, 3]:
            result = True
    return result


def string_match(a, b):
    '''Given 2 strings, a and b, return the number of the positions where they
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in both
    strings.'''
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
    string where the word is in the middle of the out string, e.g. "<<word>>".
    '''

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

# List-1


def first_last6(nums):
    '''Given an array of ints, return True if 6 appears as either the first or
    last element in the array. The array will be length 1 or more.'''
    return (nums[0] == 6 or nums[-1] == 6)


def same_first_last(nums):
    ''' Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.'''
    return (len(nums) >= 1 and (nums[0] == nums[-n]))


def make_pi():
    '''Return an int array length 3 containing the first 3 digits of pi,
    {3, 1, 4}.'''
    pint = str(int(math.pi * 100))
    results = list(map(int, pint))
    return results


def common_end(a, b):
    '''Given 2 arrays of ints, a and b, return True if they have the same first
    element or they have the same last element. Both arrays will be length 1 or
    more.'''
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


def max_end3(nums):
    '''Given an array of ints length 3, figure out which is larger, the first or
    last element in the array, and set all the other elements to be that value.
    Return the changed array.'''
    max_e = max([nums[0], nums[-1]])
    return 3 * [max_e]


def sum2(nums):
    '''Given an array of ints, return the sum of the first 2 elements in the
    array. If the array length is less than 2, just sum up the elements that
    exist, returning 0 if the array is length 0. '''
    return sum(nums[:2])


def middle_way(a, b):
    '''Given 2 int arrays, a and b, each length 3,
    return a new array length 2 containing their middle elements.'''
    return [a[1], b[1]]


def make_ends(nums):
    '''Given an array of ints, return a new array length 2 containing the first
    and last elements from the original array. The original array will be
    length 1 or more.'''

    return [nums[0], nums[-1]]


def has23(nums):
    '''Given an int array length 2, return True if it contains a 2 or a 3.'''
    return (2 in nums) or (3 in nums)


def cigar_party(cigars, is_weekend):
    '''When squirrels get together for a party, they like to have cigars. A
    squirrel party is successful when the number of cigars is between 40 and 60,
    inclusive. Unless it is the weekend, in which case there is no upper bound on
    the number of cigars. Return True if the party with the given values is
    successful, or False otherwise.'''
    return (not is_weekend and (cigars >= 40 and cigars <= 60)) or (is_weekend and cigars >= 40)


def date_fashion(you, date):
  '''You and your date are trying to get a table at a restaurant. The parameter
  "you" is the stylishness of your clothes, in the range 0..10, and "date" is
  the stylishness of your date's clothes. The result getting the table is encoded
  as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish,
  8 or more, then the result is 2 (yes). With the exception that if either of
  you has style of 2 or less, then the result is 0 (no). Otherwise the result
  is 1 (maybe).'''
  result = 1
  if (you >= 8 or date >= 8):
    result = 2
  if (you <= 2 or date <= 2):
    result = 0
  return result


def squirrel_play(temp, is_summer):
  '''The squirrels in Palo Alto spend most of the day playing. In particular,
  they play if the temperature is between 60 and 90 (inclusive). Unless it is
  summer, then the upper limit is 100 instead of 90. Given an int temperature
  and a boolean is_summer, return True if the squirrels play and False
  otherwise.'''
  return (not is_summer and (temp >= 60 and temp <= 90)) or (is_summer and (temp >= 60 and temp <= 100))


def caught_speeding(speed, is_birthday):
 '''You are driving a little too fast, and a police officer stops you. Write
 code to compute the result, encoded as an int value: 0=no ticket, 1=small
 ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is
 between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the
 result is 2. Unless it is your birthday -- on that day, your speed can be 5
 higher in all cases.'''
 result_ticket = 1
 bonus = 0
 if (is_birthday):
     bonus = 5
 if (speed <= 60 + bonus):
     result_ticket = 0
 elif (speed >= 61 + bonus and speed <= 80 + bonus):
     result_ticket = 1
 elif (speed >= 81 + bonus):
     result_ticket = 2

 return result_ticket


def sorta_sum(a, b):
 '''Given 2 ints, a and b, return their sum. However, sums in the range
 10..19 inclusive, are forbidden, so in that case just return 20.'''
 result = a + b
 if (result >= 10 and result <= 20):
    result = 20

 return result


def alarm_clock(day, vacation):
    '''Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
    boolean indicating if we are on vacation, return a string of the form "7:00"
    indicating when the alarm clock should ring. Weekdays, the alarm should be
    "7:00" and on the weekend it should be "10:00". Unless we are on vacation
    -- then on weekdays it should be "10:00" and weekends it should be "off".'''
    result_alarm = "10:00"
    if (not vacation):
        if (day >= 1 and day <= 5):
            result_alarm = "7:00"
    else:
        if (day == 0 or day == 6):
            result_alarm = "off"
    return result_alarm


def love6(a, b):
    '''The number 6 is a truly great number. Given two int values, a and b,
    return True if either one is 6. Or if their sum or difference is 6. Note:
    the function abs(num) computes the absolute value of a number.'''

    return 6 in [a + b, a, b, abs(a - b)]


def in1to10(n, outside_mode):
    '''Given a number n, return True if n is in the range 1..10, inclusive.
    Unless outside_mode is True, in which case return True if the number is
    less or equal to 1, or greater or equal to 10.'''
    result = False

    if (not outside_mode):
        if (n >= 1 and n <= 10):
            result = True
    else:
        if (not (n > 1 and n < 10)):
            result = True
    return result


def near_ten(num):
    '''Given a non-negative number "num", return True if num is within 2 of a
    multiple of 10. Note: (a % b) is the remainder of dividing a by b,
    so (7 % 5) is 2.'''
    num = abs(num)
    md = num % 10
    return (abs(10 - md) <= 2 or md <= 2)


def make_bricks(small, big, goal):
    '''We want to make a row of bricks that is goal inches long. We have a number
    of small bricks (1 inch each) and big bricks (5 inches each). Return True
    if it is possible to make the goal by choosing from the given bricks.
    This is a little harder than it looks and can be done without any loops. '''
    result = False
    if goal >= 5 * big:
        rm = goal - (5 * big)
    else:
        rm = goal % 5
    if (small >= rm):
        result = True
    return result


def lone_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. However, if one of the
    values is the same as another of the values, it does not count
    towards the sum.'''
    list_abc = [a, b, c]
    result = 0
    if(list_abc.count(a) == 1):
      result += a
    if(list_abc.count(b) == 1):
      result += b
    if(list_abc.count(c) == 1):
      result += c
     return result

def lucky_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. However, if one of the
    values is 13 then it does not count towards the sum and values to its right
    do not count. So for example, if b is 13, then both b and c do not count.'''
    list_abc = []
    toward = True
    if(a!=13):
        list_abc.append(a)
    else:
        toward = False
    if(b!=13 and toward):
      list_abc.append(b)
    else:
        toward = False
    if(c!=13 and toward):
      list_abc.append(c)

    return sum(list_abc)

def no_teen_sum():
    '''Given 3 int values, a b c, return their sum. However, if any of the values
    is a teen -- in the range 13..19 inclusive -- then that value counts as 0,
    except 15 and 16 do not count as a teens. Write a separate helper
    "def fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    Define the helper below and at the same indent level as the main no_teen_sum().'''
    def fix_teen(n):
        if (n>=13 and n<=19) and not (n==15 or n==16):
            return 0
        return n

    return fix_teen(a)+fix_teen(b)+fix_teen(c)


def round_sum(a, b, c):
    '''For this problem, we'll round an int value up to the next multiple of 10
    if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately,
    round down to the previous multiple of 10 if its rightmost digit is less
    than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of
    their rounded values. To avoid code repetition, write a separate helper
    "def round10(num):" and call it 3 times. Write the helper entirely below
    and at the same indent level as round_sum().'''
    def round_sum(num):
        ex =  num % 10
        if (ex>=5):
            ex = 10 - ex
        else:
            ex = -1 * ex
        return num + ex
    return round_sum(a)+round_sum(b)+round_sum(c)

def close_far(a, b, c):
    '''Given three ints, a b c, return True if one of b or c is "close"
    (differing from a by at most 1), while the other is "far", differing from
    both other values by 2 or more. Note: abs(num) computes the absolute value
    of a number.'''
    result = False
    a_b_diff = abs(a - b)
    a_c_diff = abs(a - c)
    b_c_diff = abs(b - c)

    if (a_b_diff<= 1 and a_c_diff >= 2 and b_c_diff >= 2):
        result = True
    elif (a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2):
        result = True
    return result

def make_chocolate(small, big, goal):
    '''We want make a package of goal kilos of chocolate. We have small bars
    (1 kilo each) and big bars (5 kilos each). Return the number of small bars
    to use, assuming we always use big bars before small bars. Return -1
    if it can't be done.'''
    num_bar = -1
    nd = goal-(big*5)
    if goal >= (big*5):
        rm = nd
    else:
        rm = goal % 5

    if rm <= small:
        return rm

    return num_bar

# String-2
def double_char(str):
  '''Given a string, return a string where for every char in the original,
  there are two chars.'''
  "".join([2*l for l in str])

def count_hi(str):
  '''Return the number of times that the string "hi" appears anywhere
  in the given string.'''
  HI = 'hi'
  return str.count(HI)

 def cat_dog(str):
     '''Return True if the string "cat" and "dog" appear the same number of
    times in the given string.'''
    result = False
    if (str.count('cat')==str.count('dog')):
        retult = True
    return result

def count_code(str):
    '''Return the number of times that the string "code" appears anywhere in
    the given string, except we'll accept any letter for the 'd', so "cope"
    and "cooe" count.'''
  result = 0
  for i in range(0,len(str)-3 ):
    if (str[i:i+2] == 'co') and (str[i+3]=='e'):
      result+=1

  return result

def end_other(a, b):
    '''Given two strings, return True if either of the strings appears at the
    very end of the other string, ignoring upper/lower case differences (in other
    words, the computation should not be "case sensitive"). Note: s.lower()
    returns the lowercase version of a string.'''
  return b.lower().endswith(a.lower())  or a.lower().endswith(b.lower())

def xyz_there(str):
    '''Return True if the given string contains an appearance of "xyz" where
    the xyz is not directly preceeded by a period (.). So "xxyz" counts but
    "x.xyz" does not.'''
    f_xyz = str.find('xyz')
    re = False
    for i in range(len(str)):
        if (str[i:i+3]=='xyz') and (str[i-1] !='.'):
            re = True
    return re

def count_evens(nums):
    '''Return the number of even ints in the given array. Note: the % "mod"
    operator computes the remainder, e.g. 5 % 2 is 1.'''
    re = 0
    for i in nums:
    if (i % 2 == 0):
      re+=1
     return re

def big_diff(nums):
    '''Given an array length 1 or more of ints, return the difference between
    the largest and smallest values in the array. Note: the built-in min(v1, v2)
    and max(v1, v2) functions return the smaller or larger of two values.'''
    return abs(max(nums)-min(nums))

def centered_average(nums):
    '''Return the "centered" average of an array of ints, which we'll say is the
    mean average of the values, except ignoring the largest and smallest values
    in the array. If there are multiple copies of the smallest value, ignore just
    one copy, and likewise for the largest value. Use int division to produce the
    final average. You may assume that the array is length 3 or more.'''
    min_val = min(nums)
    max_val = max(nums)
    del nums[nums.index(min_val)]
    del nums[nums.index(max_val)]

    return avg(nums)


def sum13(nums):
    '''Return the sum of the numbers in the array, returning 0 for an empty
    array. Except the number 13 is very unlucky, so it does not count and
    numbers that come immediately after a 13 also do not count.'''
    re_sum13 = 0
    for i in range(len(nums)):
        if (nums[i])==13 and i+1 != len(nums) and ((nums[i+1])!=13):
            re_sum13 -= nums[i+1]

        if (nums[i]!=13):
            re_sum13 += nums[i]

    return re_sum13


def sum67(nums):
    '''Return the sum of the numbers in the array, except ignore sections of
    numbers starting with a 6 and extending to the next 7 (every 6 will be
    followed by at least one 7). Return 0 for no numbers.'''
    inRange = True
    reSum67 = 0

    for n in nums:
        if n == 6:
            inRange = False

        if inRange:
            reSum67 += n
            continue

        if n == 7:
            inRange = True

    return reSum67
