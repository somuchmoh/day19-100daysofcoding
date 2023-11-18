from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.back(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=timmy.reset, key="c")
screen.exitonclick()
