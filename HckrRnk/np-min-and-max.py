import numpy

n,m = map(int,input().split(' '))

marray=numpy.array([list(map(int,input().split(' '))) for _ in range(n)])

    
print( numpy.min(marray, axis = 1).max()   )
