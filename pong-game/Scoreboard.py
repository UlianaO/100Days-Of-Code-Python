from turtle import Turtle, TurtleScreen

TITLE_ALIGNMENT = "center"
TITLE_FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Screen class
        self.score = 0
        self.hideturtle()
        self.center_title()
        self.goto(-30, 250)
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def center_title(self):
        self.penup()
        self.goto(-10, 270)

    def update_left(self):
        self.l_score += 1
        self.update_board()

    def update_right(self):
        self.r_score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.l_score}  |   {self.r_score}", move=False, align=TITLE_ALIGNMENT, font=TITLE_FONT)