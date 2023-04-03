# My version of the infamous Pong Game.

from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard

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
ball = Ball()
scoreboard = Scoreboard()
# Connecting keyboard listeners
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls. Ball should bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:  # hit the top or bottom wall
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect R paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        # go to the opposite direction
        ball.bounce_x()
        # L paddle gets a point
        scoreboard.update_left()

    # Detect L paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        # go to the opposite direction
        ball.bounce_x()
        # R paddle gets a point
        scoreboard.update_right()


# Paddle class
# Scoreboard

screen.exitonclick()