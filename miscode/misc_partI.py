#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def hasConsecutive(mlist):
            
    "Determine if the current list has at least one consecutive number"
    arm = np.array(mlist)
    arm.sort()
    
    result = False
    for i in range(0, arm.size - 1):
        if (arm[i]+1==arm[i+1]):
            result = True
            break

    return result


