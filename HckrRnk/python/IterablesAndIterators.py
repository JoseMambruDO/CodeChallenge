#!/usr/bin/env python
# -*- coding: utf-8 -*-


##You are given a list of lowercase English letters. For a given integer , you can select any indices (assume
##
##-based indexing) with a uniform probability from the list.
##
##Find the probability that at least one of the indices selected will contain the letter: '
##
##'.
##
##Input Format
##
##The input consists of three lines. The first line contains the integer
##, denoting the length of the list. The next line consists of
##
##space-separated lowercase English letters, denoting the elements of the list.
##
##The third and the last line of input contains the integer
##
##, denoting the number of indices to be selected.
##
##Output Format
##
##Output a single line consisting of the probability that at least one of the
##indices selected contains the letter:'
##
##'.
##
##Note: The answer must be correct up to 3 decimal places.
##
##Constraints
##
##All the letters in the list are lowercase English letters.


from itertools import combinations

class IterablesAndIterators():
        
    def __init__(self) -> None:
        pass

    def propablity_e_in_elements(self, elements, ns, e):
        elements = elements.split()
        pool = list(combinations(elements,ns))
        
        comb_with_e = [ep for ep in pool if e in ep]
        
        prob  = len(comb_with_e)/len(pool)
        
        return "{:.4}".format(prob)
    
