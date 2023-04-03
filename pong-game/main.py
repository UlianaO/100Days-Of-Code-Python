# My version of the infamous Pong Game.

from turtle import Screen, Turtle
from Paddle import Paddle

RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)
# Screen Defaults
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightsteelblue1")
screen.title("Ping Pong Game")
screen.tracer(0)  # animation turned off

# Creating two paddles
r_paddle = Paddle(RIGHT_PADDLE_POS)
l_paddle = Paddle(LEFT_PADDLE_POS)

# Connecting keyboard listeners
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    screen.update()


# Paddle class
# Scoreboard

screen.exitonclick()