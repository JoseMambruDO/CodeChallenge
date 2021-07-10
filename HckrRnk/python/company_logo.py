#!/bin/python3

import math>
import os
import random
import re
import sys

import collections

if __name__ == '__main__':
    s = sorted(input().strip())
    
    for t in collections.Counter([e for e in s]).most_common(3):
        print(t[0],t[1])
    
    