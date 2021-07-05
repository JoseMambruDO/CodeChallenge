#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    c = Counter(candles)
    res = 0
    for i in candles:
        if c[i]>res:
            res = c[i]
    return res
