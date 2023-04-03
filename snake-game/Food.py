# Described how the food appears on the screen.

from turtle import Turtle
import random

# screen size is 600 x 600
screen_frame_limit_x = 250
screen_frame_limit_y = 250

class Food(Turtle):

    def __init__(self):

        super().__init__()  # Turtle class
        self.colors = ["SteelBlue4", "DeepPink", "DarkOrange4", "DarkSlateGray", "BurlyWood4", "DarkOliveGreen4"]
        # Attributes of food
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)  # Default is 20X20.
        self.random_color()
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        # Position food randomly on the screen
        x = random.randint(-screen_frame_limit_x, screen_frame_limit_x)  # -280 -- 280
        y = random.randint(-screen_frame_limit_y, screen_frame_limit_y)
        self.random_color()
        self.goto(x, y)

    def random_color(self):
        self.color(random.choice(self.colors))
