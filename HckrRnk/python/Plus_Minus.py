##Complete the plusMinus function in the editor below.
##
##plusMinus has the following parameter(s):
##
##    int arr[n]: an array of integers
##
##Print
##Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with
##
##digits after the decimal. The function should not return a value.
##
##Input Format
##
##The first line contains an integer,
##, the size of the array.
##The second line contains space-separated integers that describe 


def plusMinus(arr):
    p = n = z =0    
    
    l =len(arr)
    
    for e in arr:
        if e > 0:
            p += 1
        elif e < 0:
            n += 1
        else:   
            z += 1
            
    print(p/l)
    print(n/l)
    print(z/l)