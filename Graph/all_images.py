from Graph.Globals import *
from Graph.graph import *
from Graph.canvas import *
from PIL import Image, ImageTk




red_circle = Image.open("images/red_circle.png")
red_circle = red_circle.resize((15, 15), Image.ANTIALIAS)
red_circle = ImageTk.PhotoImage(red_circle)


# def create_red_circle(c):
#     c.bind('<Button-1>', lambda event, c=c,
#            arg='red_circle': evn(event, c, arg))
#     pass


blue_X = Image.open("images/blue_X.png")
blue_X = blue_X.resize((15, 15), Image.ANTIALIAS)
blue_X = ImageTk.PhotoImage(blue_X)


# def create_blue_X(c):
#     c.bind('<Button-1>', lambda event, c=c,  arg='blue_X': evn(event, c,  arg))
#     pass


red_open_bracket = Image.open("images/red_open_bracket.png")
red_open_bracket = red_open_bracket.resize((15, 15), Image.ANTIALIAS)
red_open_bracket = ImageTk.PhotoImage(red_open_bracket)


# def create_red_open_bracket():
#     c.bind('<Button-1>', lambda event, c=c,
#            arg='red_open_bracket': evn(event, c,  arg))
#     pass


blue_close_bracket = Image.open("images/blue_close_bracket.png")
blue_close_bracket = blue_close_bracket.resize((15, 15), Image.ANTIALIAS)
blue_close_bracket = ImageTk.PhotoImage(blue_close_bracket)


# def create_blue_close_bracket():
#     c.bind('<Button-1>', lambda event, c=c,
#            arg='blue_close_bracket': evn(event, c,  arg))
#     pass


red_sq_bkt = Image.open("images/red_sq_bkt.png")
red_sq_bkt = red_sq_bkt.resize((15, 15), Image.ANTIALIAS)
red_sq_bkt = ImageTk.PhotoImage(red_sq_bkt)


# def create_red_sq_bkt():
#     c.bind('<Button-1>', lambda event, c=c,
#            arg='red_sq_bkt': evn(event, c,  arg))
#     pass


blue_sq_bkt = Image.open("images/blue_sq_bkt.png")
blue_sq_bkt = blue_sq_bkt.resize((15, 15), Image.ANTIALIAS)
blue_sq_bkt = ImageTk.PhotoImage(blue_sq_bkt)


# def create_blue_sq_bkt():
#     c.bind('<Button-1>', lambda event, c=c,
#            arg='blue_sq_bkt': evn(event, c,  arg))
#     pass

def insert_image(arg):
    c.bind('<Button-1>', lambda event, arg=arg: evn(event,  arg))
    