#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointa=0
    pointb=0
    ar = []
    for i in range(3):
        if a[i]>b[i]:
            pointa+=1
            
        if a[i]<b[i]:
            pointb+=1
    ar.insert(0,pointa)
    ar.insert(1,pointb)        
    return(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
