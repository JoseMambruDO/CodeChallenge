def diagonalDifference(arr):
    ''''Diagonal Difference funtion take a parameter arr 2D en determine differeces between sum of diagonals'''
    n=len(arr[0])
    d0=sum([arr[i][i] for i in range (0,n) ])
    d1=sum([arr[i][(n-1)-i] for i in range (0,n) ])
    
    return abs(d0-d1)