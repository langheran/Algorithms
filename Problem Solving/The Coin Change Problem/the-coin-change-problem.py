#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getWays function below.
def getWays(n, c):
    m = len(c)
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0, m):
        for j in range(c[i], n+1):
            table[j] += table[j-c[i]]
    print(table[n])
    return table[n]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(str(ways) + "\n")
