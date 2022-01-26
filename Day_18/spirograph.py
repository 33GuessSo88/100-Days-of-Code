import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

r = 50
num_of_circles = 36
angle = 360 / num_of_circles
timmy_the_turtle.speed(0)
turtle.colormode(255)

def random_color():
    color = random.sample(range(1, 255), 3)
    return color

for i in range(num_of_circles):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(r)
    timmy_the_turtle.left(angle)

screen = Screen()
screen.exitonclick()