# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:02:51 2020

@author: lexsh

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
sequence = []
def ranger (n1, n2): #2000 and 3200
    for i  in range(n1, n2):
        if (i % 7 == 0) and (i % 5 != 0):
            sequence.append(str(i))
    print(",".join(sequence))
#    print(sequence)       
ranger(2000, 32000)            