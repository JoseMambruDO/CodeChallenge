def merge_the_tools(string, k):
    ''''Complete the merge_the_tools function in the editor below.

    merge_the_tools has the following parameters:

    string s: the string to analyze
    int k: the size of substrings to analyze

    Prints

    Print each subsequence on a new line. There will be of them. No return value is expected. 
    '''
   
    l = len(string)
    chop_string = list(range(0,l,k))
    chopper = [string[i:i+k] for i in chop_string]
    new_list = []
    for substring in chopper:
        distint = ''
        for e in substring:
           if not e in distint:
                 distint += e
         
        new_list.append(distint)
        
    print("\n".join(new_list))