# -*- cofing: utf-8 -*- 

from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text = "Quit", fg = "red", command = master.destroy)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text = "OI!",  command = self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Ola mundo !")
root = Tk()
app = App(root)
root.mainloop()