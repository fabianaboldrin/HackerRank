#!/bin/python3

import sys

def miniMaxSum(arr):
    m = sum(arr)-max(arr)
    n = sum(arr)-min(arr)
    print(m, n)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
