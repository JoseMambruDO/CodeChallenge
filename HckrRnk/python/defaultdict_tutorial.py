from collections import defaultdict
d = defaultdict(list)

a, b = map(int,input().split())

l=list(range(1,(a)+1))+list(range(1,(b)+1))

for i in l:
    e = input()
    if (e == 'a') and f'{i}' not in d['a'] :
        d['a'].append(f'{i}')
        
    if (e == 'b') and f'{i}' not in d['b'] :
        
        d['b'].append(f'{i}')
    

print(' '.join(d['a']))
print(' '.join(d['b']))

