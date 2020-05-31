# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:08:44 2020

@author: lexsh
"""

def calcFactorial (n):
    i = 1
    sequence = []
    result = 1
    if (n <= 0):
        n = 1
    while i <= n:
        sequence.append(str(i))
        i += 1
        result *= i-1
    print(n,"!:", " x ".join(sequence) , " = " , result)

calcFactorial(8)
