##You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
##
##Input Format
##
##The first line contains an integer
##N. N is the total number of integers in the list.
##The second line contains the space separated list of integers.

N = int(input())

ll = list(map(int,input().split(' ')))

print(all([e>0 for e in ll]) and any([str(e)==str(e)[::-1] for e in ll]))