input()
a=list(map(int,input().split(' ')))
input()
b=list(map(int,input().split(' ')))

set_a = set(a)
set_b = set(b)

print(len(set_a|set_b))