#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
lista = []
for i in range(n):
    lista.append(arr.pop())

for p in lista: print(p,end=' ')
