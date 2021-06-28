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

