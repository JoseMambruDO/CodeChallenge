"Your task is to compute how much money earned."

from collections import Counter

X = int(input())
listShoes = map(int,input().split(' '))
counterShoes = Counter(listShoes)

N = int(input())

accumulated_sales = 0

for i in range(0,N):
    
    
    customer = list(map(int, input().split(' ')))
    purchased_size = customer[0]
    purchased_price = customer[1]
    
    if counterShoes[purchased_size] > 0:
        counterShoes[purchased_size] -= 1
        accumulated_sales += purchased_price

print(accumulated_sales)
        