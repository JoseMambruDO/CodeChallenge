import re

n = int(input())
pattern = r'^[-+]?[0-9]*\.[0-9]+$'

for _ in range(n):
    print(re.match(pattern, input())!=None)