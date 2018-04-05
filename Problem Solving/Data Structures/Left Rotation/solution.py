#!/bin/python3

import sys

def leftRotation(a, d):
    
    for i in range(d):
        el = a.pop(0)
        a.append(el)
        
    print(" ".join([str(x) for x in a] ))
        

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))


