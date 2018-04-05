#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    fib = [1,2]
    ele = 0
    soma = 0
    n = int(input().strip())
    while ele < n:
        ele = fib[-1]+fib[-2]
        if ele < n:
            fib.append(ele)
            
    for i in fib:
        if i%2 == 0: 
            soma += i
    print(soma)
