
##A valid UID must follow the rules below:
##
##    It must contain at least 
##
##uppercase English alphabet characters.
##It must contain at least
##digits ( -
##).
##It should only contain alphanumeric characters (
##- , - & -
##).
##No character should repeat.
##There must be exactly
##characters in a valid UID

import string

def valid(l):
    r = True
    
    if r and len([e for e in l if e in string.ascii_uppercase])<2:
            r=False

    if r and len([e for e in l if e in string.digits])<3:
            r=False
    
    if r and len([e for e in l if e not in string.ascii_letters+string.digits])>0:
            r=False
    
    if r and len(set(l))!=10:
            r=False
    
    return r
            

for _ in range(int(input())):
    
    if valid(str(input())):
        print('Valid')
    else:
        print('Invalid')
