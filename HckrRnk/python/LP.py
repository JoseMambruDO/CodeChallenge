
"print all possible permutations of size"
from itertools import permutations

inpt = input().split(' ')

S = inpt[0]
N = int(inpt[1])

lperm = list(permutations(S,N))

lperm = sorted(lperm)

for e in lperm:
    print("".join(list(e)))