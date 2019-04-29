#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stockmax function below.
def stockmax(prices):
    p_max=prices.index(max(prices))
    cost=sum(prices[:p_max])
    prof=len(prices[:p_max])*prices[p_max]-cost
    if len(prices[(p_max+1):])>0:
        prof+=stockmax(prices[(p_max+1):])
    return prof

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        prices = list(map(int, input().rstrip().split()))
        result = stockmax(prices)
        print(str(result) + '\n')