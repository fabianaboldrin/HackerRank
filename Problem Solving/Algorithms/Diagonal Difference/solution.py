#!/bin/python3

import sys

def diagonalDifference(a):
    n = len(a)
    d1 = 0
    d2 = 0
    
    for i in range(n):
        d1 += a[i][i]
        d2 += a[i][n-i-1]
        
    result = abs(d1-d2)

    return(result)
    

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
