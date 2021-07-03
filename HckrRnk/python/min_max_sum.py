#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    s_list = []
    for i in range(len(arr)):
        copy_arr = arr[:]
        copy_arr.pop(i)
        s_list.append(sum(copy_arr))
    
    print(min(s_list), max(s_list))
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
