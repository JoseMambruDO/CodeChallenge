##Task
##
##Perform append, pop, popleft and appendleft methods on an empty deque d.
##
##Input Format
##
##The first line contains an integer N.the number of operations.
##The next lines contains the space separated names of methods and their values.
##
##Constraints
##0<N<=1100
##Output Format
##
##Print the space separated elements of deque d.


import re
from collections import deque

d=deque()
pattern = re.compile('\s(\d+)$')
pre = "d."
suf = ""

for _ in range(int(input())):
    l = input()
    if pattern.search(l) != None:
        suf = re.sub(pattern,r'(\1)',l)
    else:
        suf = l+"()"
    
    eval(pre+suf)

list_deque = list(map(str, list(d)))
print(" ".join(list_deque))


#Best Solution using getattr

##d = deque()
##for _ in range(int(input())):
##        func, *num = input().split()
##        getattr(d, func)(*num)
##print(' '.join(d))



    