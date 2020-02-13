# !/usr/bin/python3
# ref: https://www.tutorialspoint.com/python3/tk_entry.htm
from tkinter import Tk, Entry, Label, LEFT, RIGHT

top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()