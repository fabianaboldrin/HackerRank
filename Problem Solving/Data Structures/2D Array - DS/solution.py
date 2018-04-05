#!/bin/python3

import sys

arr = []
sum = []

for arr_i in range(6):
   tmp = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(tmp)


for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        
print(max(sum))
