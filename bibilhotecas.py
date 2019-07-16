# -*- coding utf-8 -*- 


import math 
x = 5
print(math.sqrt(5))
print(math.sin(x))
print(math.log(x))
print(math.cos(x))


from tkinter import *
box = Button (texto = 'Ok', comand = 'exit')
box.pack()
box.mainloop()



import time

for i in range(1,6):
    time.sleep(1)
    print( f'Se passou {i} segundo(s).')

