from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode(rmode="user")
        self.shapesize(stretch_wid=10)
        self.setpos(x=370, y=0)

