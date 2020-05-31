# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:08:44 2020

@author: lexsh
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

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
