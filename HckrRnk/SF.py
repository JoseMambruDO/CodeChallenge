#String Formatting
def print_formatted(number):
    space_padded = len(bin(number)) - 2
    
    for i in range(1,number+1):
        print("{:>{space_padded}} {:>{space_padded}} {:>{space_padded}} {:>{space_padded}}".format(i,oct(i).replace('0o',''),hex(i).replace('0x','').upper(),bin(i).replace('0b',''), space_padded=space_padded))



if __name__ == '__main__':
    #n = int(input())
    n=17
    print_formatted(n)
