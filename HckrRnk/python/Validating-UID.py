
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

import re
import string

def valid(l):
    r = True
    
    if r:
        if len(l)!=10:
            r=False
    
    if r:
        if len([e for e in l if e in string.ascii_uppercase])<2:
            r=False
    if r:
        if len([e for e in l if e in string.digits])<3:
            r=False
    
    if r:
        if len([e for e in l if e in string.ascii_letters+string.digits])<1:
            r=False
    
    if r:
        if set(l)!=10:
            r=False
    
        
            
N = int(input())

for _ in range(N):
    l = str(input())
    
    if valid(l):
        print('Valid')
    else:
        print('Invalid')