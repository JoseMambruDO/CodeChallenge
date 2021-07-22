
na = int(input())
set_a = set(map(int,input().split()))

for _ in range(int(input())):
    func, ne = input().split()
    set_e = set(map(int,input().split()))

    #eval("set_a."+func+'('+str(set_e)+')')
    
    getattr(set_a,func)(set_e) # getattr is a cleaner option
    
print(sum(list(set_a)))