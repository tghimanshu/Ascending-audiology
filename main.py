import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import pyscreenshot as ImageGrab
import tkinter.tix as tix
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mysql.connector
import json

conn = mysql.connector.connect(host='localhost', user='root', password='', database='ascending_audiology')
cursor = conn.cursor()


def MainWindow(opened=False, openedData={}):
    # global Y
    
    # Function for Open Dialog
    def openACase():
        new_win = Toplevel()
        cursor.execute('SELECT * FROM cases')
        res = cursor.fetchall()
        tv = ttk.Treeview(new_win, show="headings")
        tv.pack()
        tv['columns'] = ("Case No.", "Name", "Date")
        tv.heading(0, text="Case No.")
        tv.heading(1, text="Name")
        tv.heading(2, text="Date")
        tv.column(0, anchor=tk.N)
        tv.column(1, anchor=tk.N)
        tv.column(2, anchor=tk.N)
        for r in res:
            tv.insert('', 'end', values=(r[0], r[1], r[4]))

        def open_the_data():
            itemIndex = tv.focus()
            openedData = tv.item(itemIndex)
            opened = True
            new_win.destroy()
            root.destroy()
            MainWindow(opened, openedData)
            pass
        Button(new_win, text="Open", command=open_the_data).pack()
        new_win.mainloop()
    if opened:
        cursor.execute("SELECT * FROM cases WHERE case_no = " + str(openedData['values'][0]))
        the_case = cursor.fetchone()
        # print(the_case)
    # Main Window Start
    root = tk.Tk()
    root.state('zoomed')
    root.title("Ascending Audiology")


    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openACase)


    menubar.add_cascade(menu = filemenu, label = "File")

    root.config(menu=menubar)
    
    # scrollbar

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    window = Frame(my_canvas)

    my_canvas.create_window((0,0), window=window, anchor="nw")

    '''
        PERSONAL DETAILS
    '''
    personal_details = ttk.Frame(window)
    personal_details.pack(padx=20)

    # Entry
    name = ttk.Entry(personal_details, width=25)
    name.grid(row=0, column=1)
    age = ttk.Entry(personal_details, width=25)
    age.grid(row=0, column=3)
    gender = ttk.Entry(personal_details, width=25)
    gender.grid(row=0, column=5)
    # date = Calendar(personal_details, selectmode='day')
    # date.grid(row=3, column=1)
    case_no = ttk.Entry(personal_details, width=25)
    case_no.grid(row=0, column=7)
    complaints = ttk.Entry(personal_details, width=100)
    complaints.grid(row=1, column=1, columnspan=7, sticky="we")

    # Label
    name_label = ttk.Label(personal_details, text="Name: ")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    age_label = ttk.Label(personal_details, text="Age: ")
    age_label.grid(row=0, column=2, padx=10, pady=10)
    gender_label = ttk.Label(personal_details, text="Gender: ")
    gender_label.grid(row=0, column=4, padx=10, pady=10)
    # date_label = ttk.Label(personal_details, text="Date: ")
    # date_label.grid(row=3, column=0, padx=10, pady=10)
    case_no_label = ttk.Label(personal_details, text="Case No: ")
    case_no_label.grid(row=0, column=6, padx=10, pady=10)
    complaints_label = ttk.Label(personal_details, text="Cheif Complaints: ")
    complaints_label.grid(row=1, column=0, padx=10, pady=10)

    '''
    GRAPHS
    '''
    if opened:
        points = json.loads(the_case[6])
        print(points)
    else:
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
        'red_circle': 0,
        'blue_X': 0,
        'red_triangle': 0,
        'blue_square': 0,
        'red_open_bracket': 0,
        'blue_close_bracket': 0,
        'red_sq_bkt': 0,
        'blue_sq_bkt': 0,
        'red_circle_nr': 0,
        'blue_X_nr': 0,
        'red_triangle_nr': 0,
        'blue_square_nr': 0,
        'red_open_bracket_nr': 0,
        'blue_close_bracket_nr': 0,
        'red_sq_bkt_nr': 0,
        'blue_sq_bkt_nr': 0 
    }


    # print(points)

    X = 378
    Y = 378
    GRID = 27

    graph_axis = PhotoImage(file='graph_axis.png')
    my_graph = Frame(window)
    my_graph.pack()
    le_graph_frame = Frame(my_graph, width=478, height=478, background="bisque")
    re_graph_frame = Frame(my_graph, width=478, height=478, background="bisque")

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
                # print(ex, ey, i[0], i[1])
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
                # print(ex, ey, i[0], i[1])
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
            'red_circle': points['red_circle']+points['red_circle_nr']+points['red_triangle']+points['red_triangle_nr'],
            'blue_X': points['blue_X']+points['blue_X_nr']+points['blue_square']+points['blue_square_nr'],
            'red_open_bracket':points['red_open_bracket']+points['red_open_bracket_nr']+points['red_sq_bkt']+points['red_sq_bkt_nr'],
            'blue_close_bracket': points['blue_close_bracket']+points['blue_close_bracket_nr']+points['blue_sq_bkt']+points['blue_sq_bkt_nr']
            }
        
        for arg in temp_points.keys():
            lines = sorted(temp_points[arg], key=lambda item: item[0])
            for i, p in enumerate(lines):
                try:
                    if ('_nr' not in lines[i][2] and '_nr' not in lines[i+1][2] and 'blue' not in lines[i][2] and 'blue' not in lines[i+1][2]):
                        c.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], width=1.4, fill='red', tags='lines')
                except IndexError:
                    pass

    def re_create_graph_lines():
        # t = c.find()
        c2.delete('lines')

        temp_points = {
            'red_circle': points['red_circle']+points['red_circle_nr']+points['red_triangle']+points['red_triangle_nr'],
            'blue_X': points['blue_X']+points['blue_X_nr']+points['blue_square']+points['blue_square_nr'],
            'red_open_bracket':points['red_open_bracket']+points['red_open_bracket_nr']+points['red_sq_bkt']+points['red_sq_bkt_nr'],
            'blue_close_bracket': points['blue_close_bracket']+points['blue_close_bracket_nr']+points['blue_sq_bkt']+points['blue_sq_bkt_nr']
            }
        
        for arg in temp_points.keys():
            lines = sorted(temp_points[arg], key=lambda item: item[0])
            for i, p in enumerate(lines):
                try:
                    if ('_nr' not in lines[i][2] and '_nr' not in lines[i + 1][2] and 'red' not in lines[i][2] and 'red' not in lines[i + 1][2]):
                        if 'X' in lines[i][2] or 'square' in lines[i][2]:
                            c2.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], width=1.4, fill='blue', tags='lines')
                        elif 'close' in lines[i][2] or 'sq' in lines[i][2]:
                            c2.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], dash=(4, 1), width=1.4, fill='blue', tags='lines')
                        else:
                            c2.create_line(p[0], p[1], lines[i + 1][0], lines[i + 1][1], width=1.4, fill='blue', tags='lines')

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
        for w in graph_button_frame.winfo_children():
            if not 'Cancel' in w.cget('text'):
                w.config(state="disable")
            
        
    def cancel_all():
        c.unbind('<Button-1>')
        c2.unbind('<Button-1>')
        for w in graph_button_frame.winfo_children():
            w.config(state='normal')
        pass

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




    def display_points():
        # print(points)
        for a in points.values():
            print(len(a))

    def bind_remove_points():
        c.unbind('<Button-1>')
        c.bind('<Button-1>', le_remove_points)
        c2.unbind('<Button-1>')
        c2.bind('<Button-1>', re_remove_points)
        for w in graph_button_frame.winfo_children():
            if not 'Cancel' in w.cget('text'):
                w.config(state="disable")


    def take_ss():
        box = (le_graph_frame.winfo_rootx(),le_graph_frame.winfo_rooty(),le_graph_frame.winfo_rootx()+le_graph_frame.winfo_width(),le_graph_frame.winfo_rooty() + le_graph_frame.winfo_height())
        box2 = (re_graph_frame.winfo_rootx(), re_graph_frame.winfo_rooty(), re_graph_frame.winfo_rootx() + re_graph_frame.winfo_width(), re_graph_frame.winfo_rooty() + re_graph_frame.winfo_height())
        c.itemconfigure('le_point', state='hidden')
        c2.itemconfigure('re_point', state='hidden')
        grab = ImageGrab.grab(bbox=box)
        grab2 = ImageGrab.grab(bbox=box2)
        grab.save('template/right_ear.png')
        grab2.save('template/left_ear.png')


    graph_button_frame = Frame(my_graph)
    graph_button_frame.grid(row=0, column=1, padx=10)

    um_ac = Button(graph_button_frame, text="Unmasked AC", command=lambda x='red_circle', y='blue_X': insert_image(x, y)).pack(fill="x", pady=2)
    m_ac = Button(graph_button_frame, text="Masked AC", command=lambda x='red_triangle', y='blue_square': insert_image(x, y)).pack(fill="x", pady=2)
    um_bc = Button(graph_button_frame, text="Unmasked BC", command=lambda x='red_open_bracket', y='blue_close_bracket': insert_image(x, y)).pack(fill="x", pady=2)
    m_bc = Button(graph_button_frame, text="Masked BC", command=lambda x='red_sq_bkt', y='blue_sq_bkt': insert_image(x, y)).pack(fill="x", pady=2)

    um_ac = Button(graph_button_frame, text="Unmasked AC NR", command=lambda x='red_circle_nr', y='blue_X_nr': insert_image(x, y)).pack(fill="x", pady=2)
    m_ac = Button(graph_button_frame, text="Masked AC NR", command=lambda x='red_triangle_nr', y='blue_square_nr': insert_image(x, y)).pack(fill="x", pady=2)
    um_bc = Button(graph_button_frame, text="Unmasked BC NR", command=lambda x='red_open_bracket_nr', y='blue_close_bracket_nr': insert_image(x, y)).pack(fill="x", pady=2)
    m_bc = Button(graph_button_frame, text="Masked BC NR", command=lambda x='red_sq_bkt_nr', y='blue_sq_bkt_nr': insert_image(x, y)).pack(fill="x", pady=2)

    rem_points = Button(graph_button_frame, text='Remove Points', command=bind_remove_points).pack(fill="x", pady=2)

    span_ss = Button(graph_button_frame, text='Get SS', command=take_ss).pack(fill="x", pady=2)

    span_ss = Button(graph_button_frame, text='Cancel', command=cancel_all).pack(fill="x", pady=10)

    '''
    COMMENTS
    '''

    comment = Frame(window)
    comment.pack(padx=20)

    comments = ttk.Entry(comment, width=100)
    comments.grid(row=0, column=1, columnspan=7, sticky="we")

    comments_label = ttk.Label(comment, text="Comments : ")
    comments_label.grid(row=0, column=0, padx=10, pady=10)



    '''
    TABLES
    '''
    tables = ttk.Frame(window)
    tables.pack(padx=20)

    '''
    OTOSCOPY TABLE
    '''

    oto_table = ttk.Frame(tables)
    oto_table.grid(row=0, column=0, padx=20)

    oto_title = ttk.Label(oto_table, text="OTOSCOPY")
    oto_title.grid(row=0, column=0, columnspan=2)

    oto_right = ttk.Entry(oto_table)
    oto_right.grid(row=2, column=0, padx=5)
    oto_left = ttk.Entry(oto_table)
    oto_left.grid(row=2, column=1, padx=5)

    oto_right_label = ttk.Label(oto_table, text="Right")
    oto_right_label.grid(row=1, column=0)
    oto_left_label = ttk.Label(oto_table, text="Left")
    oto_left_label.grid(row=1, column=1)

    '''
    TUNING FORK TABLE
    '''

    tf_table = ttk.Frame(tables)
    tf_table.grid(row=0, column=1, padx=20)

    tfr_right = ttk.Entry(tf_table)
    tfr_right.grid(row=2, column=1, padx=5)
    tfr_left = ttk.Entry(tf_table)
    tfr_left.grid(row=2, column=2, padx=5)

    tfw_right = ttk.Entry(tf_table)
    tfw_right.grid(row=3, column=1, padx=5)
    tfw_left = ttk.Entry(tf_table)
    tfw_left.grid(row=3, column=2, padx=5)

    tf_r = ttk.Label(tf_table, text="Rinne")
    tf_r.grid(row=2, column=0)
    tf_w = ttk.Label(tf_table, text="Weber")
    tf_w.grid(row=3, column=0)

    tf_right_label = ttk.Label(tf_table, text="Right")
    tf_right_label.grid(row=1, column=1)
    tf_left_label = ttk.Label(tf_table, text="Left")
    tf_left_label.grid(row=1, column=2)


    '''
    SPEECH AUDIOMETRY
    '''

    sa_table = ttk.Frame(tables)
    sa_table.grid(row=0, column=2, padx=20)

    sa_right_sat = ttk.Entry(sa_table)
    sa_right_sat.grid(row=2, column=1, padx=5)
    sa_right_srt = ttk.Entry(sa_table)
    sa_right_srt.grid(row=2, column=2, padx=5)
    sa_right_wrs = ttk.Entry(sa_table)
    sa_right_wrs.grid(row=2, column=3, padx=5)
    sa_right_ulc = ttk.Entry(sa_table)
    sa_right_ulc.grid(row=2, column=4, padx=5)

    sa_left_sat = ttk.Entry(sa_table)
    sa_left_sat.grid(row=3, column=1, padx=5)
    sa_left_srt = ttk.Entry(sa_table)
    sa_left_srt.grid(row=3, column=2, padx=5)
    sa_left_wrs = ttk.Entry(sa_table)
    sa_left_wrs.grid(row=3, column=3, padx=5)
    sa_left_ulc = ttk.Entry(sa_table)
    sa_left_ulc.grid(row=3, column=4, padx=5)


    sa_right = ttk.Label(sa_table, text="Right")
    sa_right.grid(row=2, column=0)
    sa_left = ttk.Label(sa_table, text="Left")
    sa_left.grid(row=3, column=0)

    sa_sat_label = ttk.Label(sa_table, text="SAT\n(dB HL)", justify="center")
    sa_sat_label.grid(row=1, column=1)
    sa_srt_label = ttk.Label(sa_table, text="SRT\n(dB HL)", justify="center")
    sa_srt_label.grid(row=1, column=2)
    sa_wrs_label = ttk.Label(sa_table, text="WRS\n(%) @", justify="center")
    sa_wrs_label.grid(row=1, column=3)
    sa_ulc_label = ttk.Label(sa_table, text="ULC\n(dB HL)", justify="center")
    sa_ulc_label.grid(row=1, column=4)

    '''
    RIGHT EAR AND LEFT YEAR
    '''
    ears = ttk.Frame(window)
    ears.pack(padx=20)

    right_ear = ttk.Entry(ears, width=100)
    right_ear.grid(row=0, column=1, columnspan=7, sticky="we")

    left_ear = ttk.Entry(ears, width=100)
    left_ear.grid(row=1, column=1, columnspan=7, sticky="we")

    right_ear_label = ttk.Label(ears, text="Right Ear: ")
    right_ear_label.grid(row=0, column=0, padx=10, pady=10)

    left_ear_label = ttk.Label(ears, text="Left Ear: ")
    left_ear_label.grid(row=1, column=0, padx=10, pady=10)

    '''
    RECMMENDATIONS
    '''
    recommendation = ttk.Frame(window)
    recommendation.pack(padx=20)


    rec = ttk.Entry(recommendation, width=100)
    rec.grid(row=0, column=1, columnspan=7, sticky="we")

    rec_label = ttk.Label(recommendation, text="Recommendations : ")
    rec_label.grid(row=0, column=0, padx=10, pady=10)

    from datetime import datetime

    curr_date = datetime.today().strftime('%Y-%m-%d')

    def submit_form():
        take_ss()
        with open('template/pdf.html', 'r') as f:
            html_file = f.read()
        html_file = html_file.replace('^name^', name.get())
        html_file = html_file.replace('^age^', age.get())
        html_file = html_file.replace('^gender^', gender.get())
        html_file = html_file.replace('^date^', str(curr_date))
        try:
            html_file = html_file.replace('^case^', str(cursor.lastrowid + 1))
        except:
            html_file = html_file.replace('^case^', str(1))
        html_file = html_file.replace('^complaints^', complaints.get())
        html_file = html_file.replace('^comments^', comments.get())
        html_file = html_file.replace('^r-oto^', oto_right.get())
        html_file = html_file.replace('^l-oto^', oto_left.get())
        html_file = html_file.replace('^r-rennie^', tfr_right.get())
        html_file = html_file.replace('^l-rennie^', tfr_left.get())
        html_file = html_file.replace('^r-weber^', tfw_right.get())
        html_file = html_file.replace('^l-weber^', tfw_left.get())
        html_file = html_file.replace('^r-sat^', sa_right_sat.get())
        html_file = html_file.replace('^l-sat^', sa_left_sat.get())
        html_file = html_file.replace('^r-srt^', sa_right_srt.get())
        html_file = html_file.replace('^l-srt^', sa_left_srt.get())
        html_file = html_file.replace('^r-wrs^', sa_right_wrs.get())
        html_file = html_file.replace('^l-wrs^', sa_left_wrs.get())
        html_file = html_file.replace('^r-ulc^', sa_right_wrs.get())
        html_file = html_file.replace('^l-ulc^', sa_left_wrs.get())
        html_file = html_file.replace('^right-ear^', right_ear.get())
        html_file = html_file.replace('^left-ear^', left_ear.get())
        html_file = html_file.replace('^reccomendations^', rec.get())
        with open('template/export.html', 'w') as f:
            f.write(html_file)
        insert_data_list = [name.get(), age.get(), gender.get(), str(curr_date), complaints.get(), json.dumps(points), comments.get(), oto_right.get(), oto_left.get(), tfr_right.get(), tfr_left.get(), tfw_right.get(), tfw_left.get(), sa_right_sat.get(), sa_left_sat.get(), sa_right_srt.get(), sa_left_srt.get(), sa_right_wrs.get(), sa_left_wrs.get(), sa_right_ulc.get(), sa_left_ulc.get(), right_ear.get(), left_ear.get(), rec.get()]
        cursor.execute("INSERT INTO `cases`(`name`, `age`, `gender`, `date`, `complaints`, `graphs`, `comments`, `r-oto`, `l-oto`, `r-rennie`, `l-rennie`, `r-weber`, `l-weber`, `r-sat`, `l-sat`, `r-srt`, `l-srt`, `r-wrs`, `l-wrs`, `r-ulc`, `l-ulc`, `right-ear`, `left-ear`, `recommendation`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", insert_data_list)
        conn.commit()
        driver = webdriver.Chrome('chromewebdriver.exe')
        driver.get('E:\\projects\\ascending_audiology\\template\\export.html')
        driver.maximize_window()
        driver.execute_script('window.print()')
        img = Image.open(BytesIO(driver.find_element_by_tag_name('body').screenshot_as_png))
        img.save('filename.pdf', "PDF", quality=100)

    submit = ttk.Frame(window)
    submit.pack(padx=20)

    submit_btn = Button(submit, text="Submit", command=submit_form)
    submit_btn.grid(row=0, column=0, padx=10, pady=10)


    # For Opened Cases
    if opened:
        case_no.insert(0, the_case[0])
        name.insert(0, the_case[1])
        age.insert(0, the_case[2])
        gender.insert(0, the_case[3])
        complaints.insert(0, the_case[5])
        comments.insert(0, the_case[7])
        oto_right.insert(0, the_case[8])
        oto_left.insert(0, the_case[9])
        tfr_right.insert(0, the_case[10])
        tfr_left.insert(0, the_case[11])
        tfw_right.insert(0, the_case[12])
        tfw_left.insert(0, the_case[13])
        sa_right_sat.insert(0, the_case[14])
        sa_left_sat.insert(0, the_case[15])
        sa_right_srt.insert(0, the_case[16])
        sa_left_srt.insert(0, the_case[17])
        sa_right_wrs.insert(0, the_case[18])
        sa_left_wrs.insert(0, the_case[19])
        sa_right_wrs.insert(0, the_case[20])
        sa_left_wrs.insert(0, the_case[21])
        right_ear.insert(0, the_case[22])
        left_ear.insert(0, the_case[23])
        rec.insert(0, the_case[24])
        
        def le_evn_opened(arg, p):
            oc = (p[0], p[1])
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


        def re_evn_opened(arg, p):
            oc = (p[0], p[1])
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
        
    for arg in points.keys():
        for p in points[arg]:
            if 'red' in arg:
                le_evn_opened(arg, p)
            elif 'blue' in arg:
                re_evn_opened(arg, p)

    window.mainloop()

if __name__ == "__main__":
    MainWindow()

cursor.close()
conn.close()