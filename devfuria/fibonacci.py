#-*- encoding: utf-8 -*- 

''' Fibonacci serie até 1_000_000 '''

a = b = 1

while a <= 10 **6:
    print(a)
    a, b = b , a + b

