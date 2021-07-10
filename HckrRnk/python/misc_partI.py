#!/usr/bin/env python
# -*- coding: utf-8 -*-


def averageDiff(array):    
    "Determine avg of distinct elements in array"
    
    sa = set(array)
    sa = list(sa)

    size = len(sa)

    return sum(sa)/size

def verifyPolinomial(xk,Px):
    "verify if P(x)=k"

    x,k = map(int,xk.split(" "))

    ack = 0

    blocksPx = ""


    for s in Px.split(" "):
        if s.startswith('x**'):
            s = s.replace('x**','')
            blocksPx += str(x**int(s))
            continue

        if s=='+' or  s=='-':
             blocksPx += s
             continue
        
        if s.startswith('x'):
          
            blocksPx += str(x)
        else:
            blocksPx += s

    
    blocksPx = blocksPx.replace('-','+-')
    for sum in blocksPx.split('+'):
        ack+=float(sum)


    return float(ack) == float(k)




##A valid UID must follow the rules below:
##
##    It must contain at least 
##
##uppercase English alphabet characters.
##It must contain at least
##digits ( -
##).
##It should only contain alphanumeric characters (
##- , - & -
##).
##No character should repeat.
##There must be exactly
##characters in a valid UID

import string
def valid(l):
    r = True
    
    if r and len(l)!=10:
            r=False
    
    if r and len([e for e in l if e in string.ascii_uppercase])<2:
            r=False

    if r and len([e for e in l if e in string.digits])<3:
            r=False
    
    if r and len([e for e in l if e not in string.ascii_letters+string.digits])>0:
            r=False
    
    if r and len(set(l))!=10:
            r=False
    
    return r