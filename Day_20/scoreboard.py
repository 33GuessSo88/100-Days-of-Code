from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.setpos(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)