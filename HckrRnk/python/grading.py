#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    nextMultiple5 = lambda x: ((x+5)//5)*5
    resGrade = []
    for e in grades:
        nm5 = nextMultiple5(e)
        if(nm5-e < 3 and nm5>=40):
            resGrade.append(nm5)
        else:
            resGrade.append(e)
    
    return resGrade
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
