import string
    
def print_rangoli(size):
    N = size

    M = ((N*4)-3)
    pl=  N -1

    fill_char = '-'

    def printpattern(i):
        md = string.ascii_lowercase[pl-i:pl+1]
        nd = md[1:]
        cp = fill_char.join(list(nd[::-1]+md) )
        return cp.center(M,fill_char)

    #top
    for i in range(0,N):
        print(printpattern(i))

    #button
    for i in range(N-2,-1,-1):
        print(printpattern(i))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
