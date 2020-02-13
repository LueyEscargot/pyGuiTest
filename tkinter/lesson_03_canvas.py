# !/usr/bin/python3
from tkinter import Tk, Canvas
from time import sleep

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 250)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.create_line(20,10,20,11,fill = 'white')
C.pack()
for i in range(0, 250, 5):
    C.create_line(0,i, i,250,fill = 'white')
top.mainloop()
