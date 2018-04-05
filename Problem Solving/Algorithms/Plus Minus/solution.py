#!/bin/python3

import sys

def plusMinus(arr):
    n = len(arr)
    pos = neg = zer = 0
    
    for i in arr:
        if i > 0:
            pos +=1
        elif i < 0:
            neg  +=1
        else:
            zer +=1
            
    print(format(pos/n, ".6f"))
    print(format(neg/n, ".6f"))
    print(format(zer/n, ".6f"))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
