import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()
# from Graph.canvas import *

points = {
    'red_circle':[],
    'blue_X':[],
    'red_open_bracket':[],
    'blue_close_bracket':[],
    'red_sq_bkt':[],
    'blue_sq_bkt':[]
}

points_count = {
    'red_circle':0,
    'blue_X':0,
    'red_open_bracket':0,
    'blue_close_bracket':0,
    'red_sq_bkt':0,
    'blue_sq_bkt':0
}


# print(points)

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

def check_y_for_same(arg, x_chord, y_chord):
    # c.delete('lines')
    exists_any = False
    temp_items = []
    for item in points[arg]:
        if item[0] == x_chord:
            t = c.find_withtag(item[2])
            c.delete(t)
            # temp_items.append([x_chord, y_chord, item[2]])
            # print('exists')
            exists_any = True
        else:
            temp_items.append(item)
        pass
    points[arg] = temp_items
    return exists_any

def create_graph_lines(arg):
    # t = c.find()
    c.delete('lines')
    
    lines = sorted(points[arg], key=lambda item: item[0])
    for i, p in enumerate(lines):
        try:
            c.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], fill='red', tags='lines')
        except IndexError:
            pass


def evn(e, arg):
    xx = c.canvasx(e.x)
    yy = c.canvasy(e.y)
    t = c.find_withtag('point')
    oc = get_oval_centre(c.bbox(t))
    if (arg == 'red_circle'):   
        ex = check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_circle, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_X'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_X, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_open_bracket'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_open_bracket, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_close_bracket'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_close_bracket, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_sq_bkt'):    
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_sq_bkt, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_sq_bkt'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_sq_bkt, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)

red_circle = Image.open("images/red_circle.png")
red_circle = red_circle.resize((15, 15), Image.ANTIALIAS)
red_circle = ImageTk.PhotoImage(red_circle)

blue_X = Image.open("images/blue_X.png")
blue_X = blue_X.resize((15, 15), Image.ANTIALIAS)
blue_X = ImageTk.PhotoImage(blue_X)

red_open_bracket = Image.open("images/red_open_bracket.png")
red_open_bracket = red_open_bracket.resize((15, 15), Image.ANTIALIAS)
red_open_bracket = ImageTk.PhotoImage(red_open_bracket)

blue_close_bracket = Image.open("images/blue_close_bracket.png")
blue_close_bracket = blue_close_bracket.resize((15, 15), Image.ANTIALIAS)
blue_close_bracket = ImageTk.PhotoImage(blue_close_bracket)

red_sq_bkt = Image.open("images/red_sq_bkt.png")
red_sq_bkt = red_sq_bkt.resize((15, 15), Image.ANTIALIAS)
red_sq_bkt = ImageTk.PhotoImage(red_sq_bkt)

blue_sq_bkt = Image.open("images/blue_sq_bkt.png")
blue_sq_bkt = blue_sq_bkt.resize((15, 15), Image.ANTIALIAS)
blue_sq_bkt = ImageTk.PhotoImage(blue_sq_bkt)

def insert_image(arg):
    c.bind('<Button-1>', lambda event, arg=arg: evn(event,  arg))

def insert_image(arg):
    c.bind('<Button-1>', lambda event, arg=arg: evn(event,  arg))
    


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
def display_points():
    print(points)
    for a in points.values():
        print(len(a))
blue_sq_bkt_btn = Button(canvas_symbols, text='get points', command=display_points).pack()
canvas_symbols.grid(row=4, column=0)


window.mainloop()