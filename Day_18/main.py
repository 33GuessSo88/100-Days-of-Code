import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('circle')

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a dashed line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# draw several shapes with increasing sides
# turtle.colormode(255)
# for i in range(4, 10):
#     side_length = 100
#     angle = 360/i
#     color = random.sample(range(1, 255), 3)
#     timmy_the_turtle.pencolor((color))
#     for x in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# Draw a random walk
timmy_the_turtle.speed(10)
timmy_the_turtle.width(10)
turtle.colormode(255)
for i in range(50):
    color = random.sample(range(1, 255), 3)
    timmy_the_turtle.pencolor((color))
    walk = random.choice(range(1,2))
    if walk == 1:
        timmy_the_turtle.forward(20)
    else:
        timmy_the_turtle.back(20)
    turn = random.choice(range(1,5))
    if turn == 1:
        timmy_the_turtle.right(0)
    elif turn == 2:
        timmy_the_turtle.right(90)
    elif turn == 3:
        timmy_the_turtle.right(180)
    else:
        timmy_the_turtle.right(270)

screen = Screen()
screen.exitonclick()