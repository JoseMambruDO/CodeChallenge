
"print all possible combination of size N"
from itertools import combinations_with_replacement

inpt = input().split(' ')

S = inpt[0]
N = int(inpt[1])

for k in range(1,N+1):
    lperm = list(combinations_with_replacement(S,k))

    new_lperm = [sorted(e) for e in lperm]
    new_lperm = sorted(new_lperm)
    
    for e in new_lperm:
        print("".join(e))