#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    m=[None]*n
    m[0]=t1
    m[1]=t2
    for i in range(2,n):
        if(m[i] is None):
            m[i]=m[i-2]+m[i-1]*m[i-1]
    return m[n-1]

if __name__ == '__main__':

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    print(str(result) + '\n')
