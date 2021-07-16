# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# 
# Specifications of HEX Color Code
# 
# ■ It must start with a '#' symbol.
# ■ It can have 3 or 6 digits.
# ■ Each digit is in the range of 0 to F. (1,2,3... E and F).
# ■ A-F letters can be lower case. (a,b,c,e and f are also valid digits).
# 
# Examples
# 
# Valid Hex Color Codes
# #FFF 
# #025 
# #F0A1FB 
# 
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
# 
# You are given lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
# 
# CSS Code Pattern


import re

for _ in range(int(input())):
    line = str(input()) 
    
    pattern = re.compile(r"(?<!^)(#([a-fA-F0-9]{6}|[a-fA-F0-9]{3}))")

    
    for match in pattern.finditer(line):
        print(match.group(1))