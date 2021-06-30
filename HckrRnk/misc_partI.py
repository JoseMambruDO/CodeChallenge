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


    return float(eval(Px)) == float(k)
