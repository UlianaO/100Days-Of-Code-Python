# Ping Pong class
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed(1)

    def move(self):
        """ Moves by gradually incresing/decreasing x and y coordinates."""
        # Moves up and up increasing each time
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse Y direction of the ball.
        self.y_move = self.y_move * (-1)

    def bounce_x(self):
        # Reverse X direction of the ball.
        self.x_move = self.x_move * (-1)

    def reset_position(self):
        self.goto(0, 0)