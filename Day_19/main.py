import random
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()

is_game_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
i = 0
for turtle_index in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_index)
    new_turtle.penup()
    y_coord = (-100 + (i*30))
    new_turtle.goto(x=-230, y=y_coord)
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! {winning_color} reached the end first!')
            else:
                print(f'You lost, {winning_color} reached the end first')
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
