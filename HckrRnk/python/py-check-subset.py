#!/usr/bin/env python
# -*- coding: utf-8 -*-


# You are given two sets, and .
# Your job is to find whether set is a subset of set .
#
# If set is subset of set , print True.
# If set is not a subset of set, print False.
#
# Input Format
#
# The first line will contain the number of test cases,T.
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set
#
# .
#
# Constraints
#
# Output Format
#
# Output True or False for each test case on separate lines.

for _ in range(int(input())):
    _, a, _, b = input(), set(input().split()), input(), set(input().split())

    print(a.issubset(b))
