#You are given a set and other sets.
#Your job is to find whether set is a strict superset of each of the N sets.
#
#Print True, if A is a strict superset of each of the sets. Otherwise, print False.
#
#A strict superset has at least one element that does not exist in its subset. 

a = set(map(int, input().split()))

li = []
for _ in range(int(input())):
   li.append( set(map(int, input().split())).issubset(a))

print(all(li))
