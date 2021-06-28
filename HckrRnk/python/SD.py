M = input()
set_M = map(int, input().split(' '))
set_M = set(set_M)

M = input()
set_N = map(int, input().split(' '))
set_N = set(set_N)


deltaMN = set_M - set_N
deltaNM = set_N - set_M

set_sorted = deltaMN.union(deltaNM)
set_sorted=sorted(set_sorted)

for e in set_sorted:
    print(e)
    