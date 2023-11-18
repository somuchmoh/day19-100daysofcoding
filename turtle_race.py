import turtle
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
turtle_names = ['timmy', 'folly', 'filly', 'tommy', 'rocky', 'rani']
y = -150
is_race_on = False

for i in range(0, len(turtle_names)):
    turtle_names[i] = Turtle(shape="turtle")
    turtle_names[i].penup()
    turtle_names[i].fillcolor(colors[i])
    turtle_names[i].goto(x=-230, y=y)
    y += 50


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_names:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.fillcolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner.")


screen.exitonclick()

