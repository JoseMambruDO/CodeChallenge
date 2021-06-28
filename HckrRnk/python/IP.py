from itertools import product

A = map(int,input().split(' '))
B = map(int,input().split(' '))

AB = list(product(A,B))

print(*AB, sep=' ')