#!/bin/python3

import math
import os
import random
import re
import sys
from sys import maxsize

# Complete the maxSubarray function below.
def maxSubarray(a):
    size=len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    return [sum(a[start:end+1]), sum(i for i in a[start:end+1] if i>0 or (a.index(i)==start and a.index(i)==end))]

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        print(' '.join(map(str, result)))
        print('\n')

