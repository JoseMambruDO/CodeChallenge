#You are given a positive integer .
#Your task is to print a palindromic triangle of size.
#
#For example, a palindromic triangle of size
#
#is:
#
#1
#121
#12321
#1234321
#123454321
#
#You can't take more than two lines. The first line (a for-statement) 
# is already written for you. 


from os import sep

for i in range(1,int(input())+1):
     print(((10**i - 1)//9)**2)
    
    
#Others soluctions without math
#     print ("".join(list(map(str,list(range(1,i+1))+list(range(i-1,0,-1))))))

#only on 1 for is allow
#    print("".join(f"{n}" for n in list(range(1,i+1))+list(range(i-1,0,-1))))

# str is no allowed
#     print ("".join(list(map(str,list(range(1,i+1))+list(range(i-1,0,-1))))))

# unpackaging
#      print (*(list(range(1,i+1))+list(range(i-1,0,-1))),sep="")
