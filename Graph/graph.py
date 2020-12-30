import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Graph.Globals import *
from Graph.all_images import *
from Graph.canvas import *


def mot(e):
    xg = (e.x+GRID/2)//GRID
    yg = (e.y+GRID/2)//GRID
    t = c.find_withtag('point')
    set_oval_coords(t, (xg*GRID, yg*GRID))

    
c.bind('<Motion>', mot)


for i in range(0, Y, GRID):
    c.create_line(0, i, X, i, fill='#999')
for i in range(0, X, GRID):
    c.create_line(i, 0, i, Y, fill='#999')

ov = c.create_oval(-3, -3, 3, 3, tags='point', fill='red')

canvas_symbols = ttk.Frame(window)
red_circle_btn = Button(canvas_symbols, text='Red Circle', command=lambda x='red_circle': insert_image(x)).pack()
blue_X_btn = Button(canvas_symbols, text='Blue X', command=lambda x='blue_X': insert_image(x)).pack()
red_open_bracket_btn = Button(canvas_symbols, text='Red <', command=lambda x='red_open_bracket': insert_image(x)).pack()
blue_close_bracket_btn = Button(canvas_symbols, text='Blue >', command=lambda x='blue_close_bracket': insert_image(x)).pack()
red_sq_bkt_btn = Button(canvas_symbols, text='Red [', command=lambda x='red_sq_bkt': insert_image(x)).pack()
blue_sq_bkt_btn = Button(canvas_symbols, text='Blue ]', command=lambda x='blue_sq_bkt': insert_image(x)).pack()
canvas_symbols.grid(row=4, column=0)
