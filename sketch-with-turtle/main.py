# This program allows creating a sketch using keystroke listeners.

from turtle import Turtle, Screen, goto


def move_forward():
    tommy.forward(10)


def move_backward():
    tommy.backward(10)


def turn_left():
    tommy.setheading(tommy.heading() + 10)


def turn_right():
    tommy.setheading(tommy.heading() - 10)

def clear():
    tommy.clear()
    tommy.penup()
    tommy.home()
    tommy.pendown()


tommy = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)  # triggers move_forward function when key is pressed
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

