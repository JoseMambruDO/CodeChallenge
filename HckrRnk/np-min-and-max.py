
#You are given a 2-D array with dimensions X.
#Your task is to perform the min function over axis and then find the max of that.

import numpy

n,m = map(int,input().split(' '))

marray=numpy.array([list(map(int,input().split(' '))) for _ in range(n)])

    
print( numpy.min(marray, axis = 1).max()   )
