#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    m = max(ar)
    sum = 0
    for i in ar:
        if(i == m):
            sum += 1
            
    return(sum)


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
