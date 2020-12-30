import tkinter as tk
from tkinter import *
# from PIL import ImageTk, Image
from Graph.all_images import red_circle, blue_X, blue_close_bracket, red_open_bracket, red_sq_bkt, blue_sq_bkt
from Graph.Globals import *

print(points)

X = 400
Y = 400
GRID = 25
c = tk.Canvas(window, width=X+1, height=Y+1,
              highlightthickness=0, bg='white')
c.grid(row=1, column=0, padx=15, pady=15)




ov_size = (6, 6)


def get_oval_centre(coords):
    x = (coords[0] + coords[2])//2
    y = (coords[1] + coords[3])//2
    return [x, y]


def set_oval_coords(t, xy):
    x, y = xy
    c.coords(t, (x - 5, y - 5, x + 5, y + 5))


def evn(e, arg):
    xx = c.canvasx(e.x)
    yy = c.canvasy(e.y)
    t = c.find_withtag('point')
    oc = get_oval_centre(c.bbox(t))
    # c.create_rectangle(oc[0]-5, oc[1]-5, oc[0]+5, oc[1]+5, fill='red')
    # print(arg)
    if(arg == 'red_circle'):
        c.create_image(oc[0], oc[1], image=red_circle, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])
    if(arg == 'blue_X'):
        c.create_image(oc[0], oc[1], image=blue_X, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])
    if(arg == 'red_open_bracket'):
        c.create_image(oc[0], oc[1], image=red_open_bracket, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])
    if(arg == 'blue_close_bracket'):
        c.create_image(oc[0], oc[1], image=blue_close_bracket, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])
    if(arg == 'red_sq_bkt'):
        c.create_image(oc[0], oc[1], image=red_sq_bkt, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])
    if(arg == 'blue_sq_bkt'):
        c.create_image(oc[0], oc[1], image=blue_sq_bkt, tags=arg+len(points[arg]))
        points[arg].append([oc[0], oc[1], arg+len(points[arg])])


def insert_image(arg):
    c.bind('<Button-1>', lambda event, arg=arg: evn(event,  arg))
    

