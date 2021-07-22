
na = int(input())
set_a = set(map(int,input().split()))

for _ in range(int(input())):
    func, ne = input().split()
    set_e = set(map(int,input().split()))

    getattr(set_a,func,set_e)

print(sum(list(set_a)))

