# Snake class that describes the behavior of the snake for the game.

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (20, 0)]

class Snake:

    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        """ Creates a snake body out of 3 segments
        and positions it in the middle """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.goto(position)
        snake.shape("square")
        self.full_snake.append(snake)

    def reset_snake(self):
        # Sending the unused turtle object beyond the screen since can`t remove.
        for segment in self.full_snake:
            segment.goto(1000, 1000)
        self.full_snake.clear()
        self.create_snake()
        self.head = self.full_snake[0]

    def move(self):
        """Snake moves by repositioning each segment to the position of the segment in the front"""
        for segment in range(len(self.full_snake) - 1, 0, -1):  # starting with len(segments), move the previous segment to the current place
            # move the tails to the position of the one in front of them
            new_x = self.full_snake[segment - 1].xcor()
            new_y = self.full_snake[segment - 1].ycor()
            self.full_snake[segment].goto(new_x, new_y)
        # move the head
        self.head.forward(MOVE_DISTANCE)

    def increase_size(self):
        self.add_segment(self.full_snake[-1].position())  # add segment to the last position

    # Control the snake. Can not go backwards.
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
