import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pyscreenshot as ImageGrab 


'''
NOTE: All right ear graph code is prefixed with le_
and   All left ear graph code is prefixed with re_ 
'''

window = Tk()
window.geometry('1200x1000')
# from Graph.canvas import *

points = {
    'red_circle':[],
    'blue_X':[],
    'red_triangle':[],
    'blue_square':[],
    'red_open_bracket':[],
    'blue_close_bracket':[],
    'red_sq_bkt':[],
    'blue_sq_bkt': [],   
    'red_circle_nr':[],
    'blue_X_nr':[],
    'red_triangle_nr':[],
    'blue_square_nr':[],
    'red_open_bracket_nr':[],
    'blue_close_bracket_nr':[],
    'red_sq_bkt_nr':[],
    'blue_sq_bkt_nr':[]
}

points_count = {
    'red_circle':0,
    'blue_X':0,
    'red_triangle':0,
    'blue_square':0,
    'red_open_bracket':0,
    'blue_close_bracket':0,
    'red_sq_bkt':0,
    'blue_sq_bkt':0,  
    'red_circle_nr':0,
    'blue_X_nr':0,
    'red_triangle_nr':0,
    'blue_square_nr':0,
    'red_open_bracket_nr':0,
    'blue_close_bracket_nr':0,
    'red_sq_bkt_nr':0,
    'blue_sq_bkt_nr':0
}


# print(points)

X = 378
Y = 378
GRID = 27

graph_axis = PhotoImage(file='graph_axis.png')

le_graph_frame = Frame(window, width=478, height=478, background="bisque")
re_graph_frame = Frame(window, width=478, height=478, background="bisque")

le_graph_frame.grid(row=0, column=0)
re_graph_frame.grid(row=0, column=2)

le_graph_label = Label(le_graph_frame, image=graph_axis)
re_graph_label = Label(re_graph_frame, image=graph_axis)

le_graph_label.place(x=0, y=0, relwidth=1, relheight=1)
re_graph_label.place(x=0, y=0, relwidth=1, relheight=1)

c = tk.Canvas(le_graph_frame, width=X+1, height=Y+1,
              highlightthickness=0, bg='white')
c.place(x=75, y=25)

c2 = tk.Canvas(re_graph_frame, width=X+1, height=Y+1,
              highlightthickness=0, bg='white')
c2.place(x=75, y=25)


ov_size = (6, 6)


for i in range(0, Y, GRID):
    c.create_line(0, i, X, i, fill='#999')
for i in range(0, X, GRID):
    if (i%2==0 and i != 0):
        c.create_line(i, 0, i, Y, dash=(1,1), fill='#999')
    else:
        c.create_line(i, 0, i, Y, fill='#999')

for i in range(0, Y+GRID, GRID):
    c2.create_line(0, i, X, i, fill='#999')
for i in range(0, X+GRID, GRID):
    if (i%2==0 and i != 0):
        c2.create_line(i, 0, i, Y, dash=(1,1), fill='#999')
    else:
        c2.create_line(i, 0, i, Y, fill='#999')

ov = c.create_oval(-3, -3, 3, 3, tags='le_point', fill='red')
ov = c2.create_oval(-3, -3, 3, 3, tags='re_point', fill='red')


def le_get_oval_centre(coords):
    x = (coords[0] + coords[2])//2
    y = (coords[1] + coords[3])//2
    return [x, y]

def re_get_oval_centre(coords):
    x = (coords[0] + coords[2])//2
    y = (coords[1] + coords[3])//2
    return [x, y]


def le_set_oval_coords(t, xy):
    x, y = xy
    c.coords(t, (x - 5, y - 5, x + 5, y + 5))

def re_set_oval_coords(t, xy):
    x, y = xy
    c2.coords(t, (x - 5, y - 5, x + 5, y + 5))

def le_check_y_for_same(arg, x_chord, y_chord):
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

def re_check_y_for_same(arg, x_chord, y_chord):
    exists_any = False
    temp_items = []
    for item in points[arg]:
        if item[0] == x_chord:
            t = c2.find_withtag(item[2])
            c2.delete(t)
            # temp_items.append([x_chord, y_chord, item[2]])
            # print('exists')
            exists_any = True
        else:
            temp_items.append(item)
        pass
    points[arg] = temp_items
    return exists_any

def le_remove_points(e):
    # ex = e.x
    # ey = e.y
    t = c.find_withtag('le_point')
    ex,ey = le_get_oval_centre(c.bbox(t))
    for arg in points.keys():
        temp = []
        for i in points[arg]:
            print(ex, ey, i[0], i[1])
            if (i[0] == ex and i[1] == ey):
                c.delete(i[2])
                continue
            temp.append(i)
        points[arg] = temp
    le_create_graph_lines()

def re_remove_points(e):
    # ex = e.x
    # ey = e.y
    t = c2.find_withtag('re_point')
    ex,ey = re_get_oval_centre(c2.bbox(t))
    for arg in points.keys():
        temp = []
        for i in points[arg]:
            print(ex, ey, i[0], i[1])
            if (i[0] == ex and i[1] == ey):
                c2.delete(i[2])
                continue
            temp.append(i)
        points[arg] = temp
    re_create_graph_lines()

def le_create_graph_lines():
    # t = c.find()
    c.delete('lines')

    temp_points = {
        'red_circle': points['red_circle']+points['red_circle_nr'],
        'red_triangle': points['red_triangle']+points['red_triangle_nr'],
         'blue_X': points['blue_X']+points['blue_X_nr'],
         'blue_square': points['blue_square']+points['blue_square_nr'],
         'red_open_bracket':points['red_open_bracket']+points['red_open_bracket_nr'],
         'blue_close_bracket': points['blue_close_bracket']+points['blue_close_bracket_nr'],
         'red_sq_bkt': points['red_sq_bkt']+points['red_sq_bkt_nr'],
         'blue_sq_bkt': points['blue_sq_bkt']+points['blue_sq_bkt_nr']
         }
    
    for arg in temp_points.keys():
        lines = sorted(temp_points[arg], key=lambda item: item[0])
        for i, p in enumerate(lines):
            try:
                if ('_nr' not in lines[i][2] and '_nr' not in lines[i+1][2] and 'blue' not in lines[i][2] and 'blue' not in lines[i+1][2]):
                    c.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], fill='red', tags='lines')
            except IndexError:
                pass

def re_create_graph_lines():
    # t = c.find()
    c2.delete('lines')

    temp_points = {
        'red_circle': points['red_circle']+points['red_circle_nr'],
        'red_triangle': points['red_triangle']+points['red_triangle_nr'],
         'blue_X': points['blue_X']+points['blue_X_nr'],
         'blue_square': points['blue_square']+points['blue_square_nr'],
         'red_open_bracket':points['red_open_bracket']+points['red_open_bracket_nr'],
         'blue_close_bracket': points['blue_close_bracket']+points['blue_close_bracket_nr'],
         'red_sq_bkt': points['red_sq_bkt']+points['red_sq_bkt_nr'],
         'blue_sq_bkt': points['blue_sq_bkt']+points['blue_sq_bkt_nr']
         }
    
    for arg in temp_points.keys():
        lines = sorted(temp_points[arg], key=lambda item: item[0])
        for i, p in enumerate(lines):
            try:
                if ('_nr' not in lines[i][2] and '_nr' not in lines[i+1][2] and 'red' not in lines[i][2] and 'red' not in lines[i+1][2]):
                    c2.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], fill='red', tags='lines')
            except IndexError:
                pass


def le_evn(e, arg):
    xx = c.canvasx(e.x)
    yy = c.canvasy(e.y)
    t = c.find_withtag('le_point')
    oc = le_get_oval_centre(c.bbox(t))
    if (arg == 'red_circle'):   
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_circle, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if (arg == 'red_triangle'):   
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_triangle, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if(arg == 'red_open_bracket'):
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_open_bracket, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if(arg == 'red_sq_bkt'):    
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_sq_bkt, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    # No Response
    if (arg == 'red_circle_nr'):   
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_circle_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if (arg == 'red_triangle_nr'):   
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_triangle_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if(arg == 'red_open_bracket_nr'):
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_open_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()
    if(arg == 'red_sq_bkt_nr'):    
        le_check_y_for_same(arg, oc[0], oc[1])
        c.create_image(oc[0], oc[1], image=red_sq_bkt_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        le_create_graph_lines()


def re_evn(e, arg):
    xx = c2.canvasx(e.x)
    yy = c2.canvasy(e.y)
    t = c2.find_withtag('re_point')
    oc = re_get_oval_centre(c2.bbox(t))
    if(arg == 'blue_X'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_X, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_square'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_square, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_close_bracket'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_close_bracket, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_sq_bkt'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_sq_bkt, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    # No Response
    if(arg == 'blue_X_nr'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_X_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_square_nr'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_square_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_close_bracket_nr'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_close_bracket_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()
    if(arg == 'blue_sq_bkt_nr'):
        re_check_y_for_same(arg, oc[0], oc[1])
        c2.create_image(oc[0], oc[1], image=blue_sq_bkt_nr, tags=arg+str(points_count[arg]))
        points[arg].append([oc[0], oc[1], arg+str(points_count[arg])])
        points_count[arg]+=1
        re_create_graph_lines()


red_circle = Image.open("images/red_circle.png")
red_circle = red_circle.resize((15, 15), Image.ANTIALIAS)
red_circle = ImageTk.PhotoImage(red_circle)

blue_X = Image.open("images/blue_X.png")
blue_X = blue_X.resize((15, 15), Image.ANTIALIAS)
blue_X = ImageTk.PhotoImage(blue_X)

red_triangle = Image.open("images/red_triangle.png")
red_triangle = red_triangle.resize((15, 15), Image.ANTIALIAS)
red_triangle = ImageTk.PhotoImage(red_triangle)

blue_square = Image.open("images/blue_square.png")
blue_square = blue_square.resize((15, 15), Image.ANTIALIAS)
blue_square = ImageTk.PhotoImage(blue_square)

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

red_triangle_nr = Image.open("images/red_triangle_nr.png")
red_triangle_nr = red_triangle_nr.resize((30, 30), Image.ANTIALIAS)
red_triangle_nr = ImageTk.PhotoImage(red_triangle_nr)

blue_square_nr = Image.open("images/blue_square_nr.png")
blue_square_nr = blue_square_nr.resize((30, 30), Image.ANTIALIAS)
blue_square_nr = ImageTk.PhotoImage(blue_square_nr)

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


def insert_image(arg1, arg2):
    c.bind('<Button-1>', lambda event, arg=arg1: le_evn(event, arg))
    c2.bind('<Button-1>', lambda event, arg=arg2: re_evn(event, arg2))
    


def le_mot(e):
    xg = (e.x+GRID/2)//GRID
    yg = (e.y+GRID/2)//GRID
    t = c.find_withtag('le_point')
    le_set_oval_coords(t, (xg*GRID, yg*GRID))

def re_mot(e):
    xg = (e.x+GRID/2)//GRID
    yg = (e.y+GRID/2)//GRID
    t = c2.find_withtag('re_point')
    re_set_oval_coords(t, (xg*GRID, yg*GRID))

    
c.bind('<Motion>', le_mot)
c2.bind('<Motion>', re_mot)


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
    c.bind('<Button-1>', le_remove_points)
    c2.unbind('<Button-1>')
    c2.bind('<Button-1>', re_remove_points)

def export_image():
    box = (c.winfo_rootx(),c.winfo_rooty(),c.winfo_rootx()+c.winfo_width(),c.winfo_rooty() + c.winfo_height())
    grab = ImageGrab.grab(bbox=box)
    grab.save('fileName.png')

def take_ss():
    box = (le_graph_frame.winfo_rootx(),le_graph_frame.winfo_rooty(),le_graph_frame.winfo_rootx()+le_graph_frame.winfo_width(),le_graph_frame.winfo_rooty() + le_graph_frame.winfo_height())
    box2 = (re_graph_frame.winfo_rootx(), re_graph_frame.winfo_rooty(), re_graph_frame.winfo_rootx() + re_graph_frame.winfo_width(), re_graph_frame.winfo_rooty() + re_graph_frame.winfo_height())
    c.itemconfigure('le_point', state='hidden')
    c2.itemconfigure('re_point', state='hidden')
    grab = ImageGrab.grab(bbox=box)
    grab2 = ImageGrab.grab(bbox=box2)
    grab.save('template/right_ear.png')
    grab2.save('template/left_ear.png')

blue_sq_bkt_btn = Button(canvas_symbols, text='get points', command=display_points).grid(row=4, column=2)
blue_sq_bkt_btn = Button(canvas_symbols, text='Remove Points', command=bind_remove_points).grid(row=4, column=3)
blue_sq_bkt_btn = Button(canvas_symbols, text='Export Image', command=export_image).grid(row=4, column=4)
canvas_symbols.grid(row=4, column=0)

graph_button_frame = Frame(window)
graph_button_frame.grid(row=0, column=1, padx=10)

um_ac = Button(graph_button_frame, text="Unmasked AC", command=lambda x='red_circle', y='blue_X': insert_image(x, y)).pack()
m_ac = Button(graph_button_frame, text="Masked AC", command=lambda x='red_triangle', y='blue_square': insert_image(x, y)).pack()
um_bc = Button(graph_button_frame, text="Unmasked BC", command=lambda x='red_open_bracket', y='blue_close_bracket': insert_image(x, y)).pack()
m_bc = Button(graph_button_frame, text="Masked BC", command=lambda x='red_sq_bkt', y='blue_sq_bkt': insert_image(x, y)).pack()

um_ac = Button(graph_button_frame, text="Unmasked AC NR", command=lambda x='red_circle_nr', y='blue_X_nr': insert_image(x, y)).pack()
m_ac = Button(graph_button_frame, text="Masked AC NR", command=lambda x='red_triangle_nr', y='blue_square_nr': insert_image(x, y)).pack()
um_bc = Button(graph_button_frame, text="Unmasked BC NR", command=lambda x='red_open_bracket_nr', y='blue_close_bracket_nr': insert_image(x, y)).pack()
m_bc = Button(graph_button_frame, text="Masked BC NR", command=lambda x='red_sq_bkt_nr', y='blue_sq_bkt_nr': insert_image(x, y)).pack()

rem_points = Button(graph_button_frame, text='Remove Points', command=bind_remove_points).pack()

span_ss = Button(graph_button_frame, text='Get SS', command=take_ss).pack()

window.mainloop()