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
    
    if (e == 'c') and f'{i-1' not in d['c'] :
        
        d['c'].append(f'{-1}')
    

print(' '.join(d['a']))
print(' '.join(d['b']))
print(' '.join(d['c']))

a 1       group A contains 'a', 'a', 'b', 'a', 'b'
a 2
b 
a
b
a       group B contains 'a', 'b'
b
