#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    res = s
    if res.endswith('PM'):
        res = res.replace('PM','')
        if int(res[0:2])==12:
            res = '12'+f'{res[2:]}'
        else:
            res = f'{int(res[0:2])+12}{res[2:]}'
    elif res.endswith('AM'):
        res = res.replace('AM','')
        if (int(res[0:2]) == 12):
           res = '00'+f'{res[2:]}'

    return res
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()