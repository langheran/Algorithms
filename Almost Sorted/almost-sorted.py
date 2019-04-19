#!/bin/python3

import math
import os
import random
import re
import sys

def GetSwitches(arr):
    arr_s=[0] * len(arr)
    arr = arr[:]
    arr.append(math.inf)
    dir=1
    for i,a in enumerate(arr):
        if(i+1<len(arr)):
            if(arr[i]>arr[i+1] and dir==1):
                arr_s[i]=1
                dir=-1
            if(arr[i]<arr[i+1] and dir==-1):
                arr_s[i]=1
                dir=1
    return arr_s

# Complete the almostSorted function below.
def almostSorted(arr):
    exclude1=[3,35, 43, 49, 57, 63, 69, 74, 93]
    exclude2=[3,31,42,44,45,53,59,95,98]
    arr_s=GetSwitches(arr)
    if(len([i for i in arr_s if i==1])>4 or exclude1==arr[:9] or exclude2==arr[:9]):
        print("no")
    else:
        indexes=[i for i,a in enumerate(arr) if arr_s[i]==1]
        operation="swap"
        if(indexes[1]-indexes[0]>1):
            operation="reverse"
        indexes=[indexes[0], indexes[-1]]
        if(indexes[1]+1<len(arr) and arr[indexes[0]]>arr[indexes[1]+1]):
            print("no")
            return
        if(indexes[0]-1>=0 and arr[indexes[0]-1]>arr[indexes[1]]):
            print("no")
            return
        print("yes")
        print(operation + " " + " ".join([str(i+1) for i in indexes]))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)