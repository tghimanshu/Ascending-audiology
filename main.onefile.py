import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pyscreenshot as ImageGrab 


window = Tk()
# from Graph.canvas import *

points = {
    'red_circle':[],
    'blue_X':[],
    'red_open_bracket':[],
    'blue_close_bracket':[],
    'red_sq_bkt':[],
    'blue_sq_bkt': [],   
    'red_circle_nr':[],
    'blue_X_nr':[],
    'red_open_bracket_nr':[],
    'blue_close_bracket_nr':[],
    'red_sq_bkt_nr':[],
    'blue_sq_bkt_nr':[]
}

points_count = {
    'red_circle':0,
    'blue_X':0,
    'red_open_bracket':0,
    'blue_close_bracket':0,
    'red_sq_bkt':0,
    'blue_sq_bkt':0,  
    'red_circle_nr':0,
    'blue_X_nr':0,
    'red_open_bracket_nr':0,
    'blue_close_bracket_nr':0,
    'red_sq_bkt_nr':0,
    'blue_sq_bkt_nr':0
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

def remove_points(e):
    # ex = e.x
    # ey = e.y
    t = c.find_withtag('point')
    ex,ey = get_oval_centre(c.bbox(t))
    for arg in points.keys():
        temp = []
        for i in points[arg]:
            print(ex, ey, i[0], i[1])
            if (i[0] == ex and i[1] == ey):
                c.delete(i[2])
                continue
            temp.append(i)
        points[arg] = temp
    create_graph_lines('red_circle')

def create_graph_lines(arg):
    # t = c.find()
    c.delete('lines')

    temp_points = {
        'red_circle': points['red_circle']+points['red_circle_nr'],
         'blue_X': points['blue_X']+points['blue_X_nr'],
         'red_open_bracket':points['red_open_bracket']+points['red_open_bracket_nr'],
         'blue_close_bracket': points['blue_close_bracket']+points['blue_close_bracket_nr'],
         'red_sq_bkt': points['red_sq_bkt']+points['red_sq_bkt_nr'],
         'blue_sq_bkt': points['blue_sq_bkt']+points['blue_sq_bkt_nr']
         }
    
    for arg in temp_points.keys():
        lines = sorted(temp_points[arg], key=lambda item: item[0])
        for i, p in enumerate(lines):
            try:
                if ('_nr' not in lines[i][2] and '_nr' not in lines[i+1][2]):
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
    # No Response
    if (arg == 'red_circle_nr'):   
        ex = check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_circle_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_X_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_X_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_open_bracket_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_open_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_close_bracket_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_close_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'red_sq_bkt_nr'):    
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_sq_bkt_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        create_graph_lines(arg)
    if(arg == 'blue_sq_bkt_nr'):
        check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=blue_sq_bkt_nr, tags=arg+str(points_count[arg]))
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

# No Response


red_circle_nr = Image.open("images/red_circle_nr.png")
red_circle_nr = red_circle_nr.resize((30, 30), Image.ANTIALIAS)
red_circle_nr = ImageTk.PhotoImage(red_circle_nr)

blue_X_nr = Image.open("images/blue_X_nr.png")
blue_X_nr = blue_X_nr.resize((30, 30), Image.ANTIALIAS)
blue_X_nr = ImageTk.PhotoImage(blue_X_nr)

red_open_bracket_nr = Image.open("images/red_open_bracket_nr.png")
red_open_bracket_nr = red_open_bracket_nr.resize((30, 30), Image.ANTIALIAS)
red_open_bracket_nr = ImageTk.PhotoImage(red_open_bracket_nr)

blue_close_bracket_nr = Image.open("images/blue_close_bracket_nr.png")
blue_close_bracket_nr = blue_close_bracket_nr.resize((30, 30), Image.ANTIALIAS)
blue_close_bracket_nr = ImageTk.PhotoImage(blue_close_bracket_nr)

red_sq_bkt_nr = Image.open("images/red_sq_bkt_nr.png")
red_sq_bkt_nr = red_sq_bkt_nr.resize((40, 40), Image.ANTIALIAS)
red_sq_bkt_nr = ImageTk.PhotoImage(red_sq_bkt_nr)

blue_sq_bkt_nr = Image.open("images/blue_sq_bkt_nr.png")
blue_sq_bkt_nr = blue_sq_bkt_nr.resize((40, 40), Image.ANTIALIAS)
blue_sq_bkt_nr = ImageTk.PhotoImage(blue_sq_bkt_nr)


def insert_image(arg):
    c.bind('<Button-1>', lambda event, arg=arg: evn(event, arg))
    


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
red_circle_btn = Button(canvas_symbols, text='Red Circle', command=lambda x='red_circle': insert_image(x)).grid(row=2, column=0)
blue_X_btn = Button(canvas_symbols, text='Blue X', command=lambda x='blue_X': insert_image(x)).grid(row=2, column=1)
red_open_bracket_btn = Button(canvas_symbols, text='Red <', command=lambda x='red_open_bracket': insert_image(x)).grid(row=2, column=2)
blue_close_bracket_btn = Button(canvas_symbols, text='Blue >', command=lambda x='blue_close_bracket': insert_image(x)).grid(row=2, column=3)
red_sq_bkt_btn = Button(canvas_symbols, text='Red [', command=lambda x='red_sq_bkt': insert_image(x)).grid(row=2, column=4)
blue_sq_bkt_btn = Button(canvas_symbols, text='Blue ]', command=lambda x='blue_sq_bkt': insert_image(x)).grid(row=2, column=5)

# No Response
red_circle_nr_btn = Button(canvas_symbols, text='Red Circle', command=lambda x='red_circle_nr': insert_image(x)).grid(row=3, column=0)
blue_X_nr_btn = Button(canvas_symbols, text='Blue X', command=lambda x='blue_X_nr': insert_image(x)).grid(row=3, column=1)
red_open_bracket_nr_btn = Button(canvas_symbols, text='Red <', command=lambda x='red_open_bracket_nr': insert_image(x)).grid(row=3, column=2)
blue_close_bracket_nr_btn = Button(canvas_symbols, text='Blue >', command=lambda x='blue_close_bracket_nr': insert_image(x)).grid(row=3, column=3)
red_sq_bkt_nr_btn = Button(canvas_symbols, text='Red [', command=lambda x='red_sq_bkt_nr': insert_image(x)).grid(row=3, column=4)
blue_sq_bkt_nr_btn = Button(canvas_symbols, text='Blue ]', command=lambda x='blue_sq_bkt_nr': insert_image(x)).grid(row=3, column=5)
def display_points():
    print(points)
    for a in points.values():
        print(len(a))
def bind_remove_points():
    c.unbind('<Button-1>')
    c.bind('<Button-1>', remove_points)

def export_image():
    box = (c.winfo_rootx(),c.winfo_rooty(),c.winfo_rootx()+c.winfo_width(),c.winfo_rooty() + c.winfo_height())
    grab = ImageGrab.grab(bbox=box)
    grab.save('fileName.png')


blue_sq_bkt_btn = Button(canvas_symbols, text='get points', command=display_points).grid(row=4, column=2)
blue_sq_bkt_btn = Button(canvas_symbols, text='Remove Points', command=bind_remove_points).grid(row=4, column=3)
blue_sq_bkt_btn = Button(canvas_symbols, text='Export Image', command=export_image).grid(row=4, column=4)
canvas_symbols.grid(row=4, column=0)


window.mainloop()