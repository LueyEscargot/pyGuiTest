# !/usr/bin/python3
from tkinter import Tk, Button

from tkinter import messagebox

top = Tk()
top.geometry("200x100")
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()