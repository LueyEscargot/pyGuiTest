# !/usr/bin/python3

import tkinter as tk
from tkinter import Tk
from tkinter import Canvas
from tkinter import PanedWindow
from tkinter import BOTH
from tkinter import Entry
from tkinter import YES
from tkinter import ttk
from tkinter import messagebox
from time import sleep


import logging
logger = logging.getLogger('event_test')
logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('[%(asctime)s-%(levelname)s] %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)

t = Tk()

CM = t.winfo_fpixels('1c')
t.minsize(int(5 * CM) , int(5 * CM))

f = tk.Frame()


top = PanedWindow(t)
top.pack(expand=1)

C = Canvas(top, bg="blue", height=250, width=250)
top.add(C)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(10, 10, 200, 200, fill='white')
C.create_line(20, 10, 20, 11, fill='white')
# C.pack(fill=BOTH, expand=YES)
for i in range(0, 250, 5):
    C.create_line(0, i, i, 250, fill='white')


def mouse_motion(event):
    logger.info("motion: {}".format(event))


def mouse_b1_motion(event):
    C.create_line(0, 0, event.x, event.y, fill='red')


logging.debug("resize")

def mouse_configure(event):
    # logger.info(event)
    # if event.widget == top:
    #     logging.debug("resize")
    #     C.configure(width=event.width-4, height=event.height-4)
    # else:
    #     logger.info("top: {}".format(top))
    #     logger.info("event.widget: {}".format(event.widget))

    if event.widget is top:
        logger.info("resize - start")
        C.configure(width=event.width-4, height=event.height-4)
        logger.info("resize - finish")
    elif event.widget is C:
        logger.info("C")
    else:
        logger.info("---")



C.bind("<B1-Motion>", mouse_b1_motion)
C.bind("<Configure>", mouse_configure)

top.bind("<Configure>", mouse_configure)

top.mainloop()
