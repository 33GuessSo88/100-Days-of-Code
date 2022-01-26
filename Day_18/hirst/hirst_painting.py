import colorgram

# colors = colorgram.extract('image.jpg', 30)
#
# color_tuple = []
# for color in colors:
#     c = color.rgb
#     red = c.r
#     green = c.g
#     blue = c.b
#     c_list = (red, green, blue)
#     color_tuple.append(c_list)
#
# print(color_tuple)

color_list = [(154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

import turtle as turtle_module
from turtle import Turtle, Screen
import random

tim = turtle_module.Turtle()

tim.speed(10)
tim.width(10)
turtle_module.colormode(255)

def draw_circle():
    color = random.choice(color_list)
    tim.dot(20, color)

def draw_one_row():
    tim.seth(0)
    for i in range(10):
        tim.pendown()
        draw_circle()
        tim.penup()
        tim.forward(50)

def reposition():
    position = tim.pos()
    new_x_position = 0
    new_y_position = position[1] + 50
    new_position = (new_x_position, new_y_position)
    tim.setpos(new_position)


for i in range(10):
    draw_one_row()
    reposition()

screen = Screen()
screen.exitonclick()