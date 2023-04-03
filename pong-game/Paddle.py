# Describes paddles for the Ping Pong game
from turtle import Turtle
from Scoreboard import Scoreboard


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # creates a narrow rectangle
        self.color("DeepPink4")
        self.penup()
        self.goto(position)
        print("Paddle Created2")
        self.score = 0

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


