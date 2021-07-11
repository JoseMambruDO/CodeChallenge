## There is an array of integers. There are also disjoint sets, and , 
## each containing integers. You like all the integers in set and dislike 
## all the integers in set . Your initial happiness is . For each integer in 
## the array, if , you add to your happiness. If , you add to your happiness. 
## Otherwise, your happiness does not change. Output your final happiness at the end. 


n,m = map(int,input().split(' '))

a = list( map(int,input().split(' ')))

set_n = set(map(int,input().split(' ')))

set_m = set(map(int,input().split(' ')))


e_n = [i for i in a if i in set_n]

e_m = [i for i in a if i in set_m]


print(len(e_n)-len(e_m))