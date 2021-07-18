#!/user/bin/env python
#-*- coding: utf-8 -*-


# You are given a string . Suppose a character '' occurs consecutively times 
# in the string. Replace these consecutive occurrences of the character '' with in the string. 
# For a better understanding of the problem, check the explanation. 

from itertools import groupby

class CompresstheString():
    def __init__(self) -> None:
        pass

    def giveCompress(self, s):
        keyfunc = lambda x: x[0]
        li_tu_gr = ["({1}, {0})".format(k,len(list(gr))) for k, gr in groupby(s,keyfunc)]

        return " ".join(li_tu_gr)
