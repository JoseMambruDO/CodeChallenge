#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys


def testlines(regex, lines):
    cpre = re.compile(regex)

    for l in lines:
        m =  cpre.match(l)
        if m:
            print(m.group())

if __name__ == "__main__":

    if (len(sys.argv) != 2):  #Read arguments
       raise Exception("Sorry, invalid arguments!!") 

    regex = sys.argv[1]
    lines = sys.stdin.readlines() #Read lines stdin 
    N = lines[1]
    testlines (regex,lines[1:N+1])