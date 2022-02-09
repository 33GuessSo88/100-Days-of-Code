from turtle import Turtle, Screen
from paddle import  Paddle

# create screen object from the Screen class
screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")

right_paddle = Paddle()



screen.exitonclick()