import math 

AB=int(input())
BC=int(input())

degre = math.degrees(math.atan(AB/BC))

DEGRE_SYMBOL= u"\N{DEGREE SIGN}"

if (degre - int(degre)>=0.5):
    print(f'{math.ceil(degre)}{DEGRE_SYMBOL}')
else:
     print(f'{math.floor(degre)}{DEGRE_SYMBOL}')


