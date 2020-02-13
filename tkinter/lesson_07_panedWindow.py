# !/usr/bin/python3
# ref: https://www.tutorialspoint.com/python3/tk_panedwindow.htm

from tkinter import PanedWindow, BOTH, Entry, Scale, VERTICAL, HORIZONTAL, Button

m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)

left = Entry(m1, bd = 5)
m1.add(left)

mid = Entry(m1, bd = 15)
m1.add(mid)

m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)

top = Scale( m2, orient = HORIZONTAL)
m2.add(top)

bottom = Button(m2, text = "OK")
m2.add(bottom)

m1.mainloop()