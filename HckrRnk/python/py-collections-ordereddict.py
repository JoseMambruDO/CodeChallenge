##You are the manager of a supermarket.
##You have a list of
##
##items together with their prices that consumers bought on a particular day.
##Your task is to print each item_name and net_price in order of its first occurrence.
##
##item_name = Name of the item.
##net_price = Quantity of the item sold multiplied by the price of each item.

from collections import OrderedDict

N = int(input())

ordered_dictionary = OrderedDict()
    
for _ in range(N):
    line = input().split(' ')
    producto=' '.join(line[:-1])
    price=int(line[-1])
    
    if producto in ordered_dictionary.keys():
        ordered_dictionary[producto] += price
    else:
         ordered_dictionary[producto] = price    
    
    
for k in ordered_dictionary.keys():
    print(k,ordered_dictionary[k])
    