from turtle import Turtle, TurtleScreen

TITLE_ALIGNMENT = "center"
TITLE_FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Screen class
        self.score = 0
        self.hideturtle()
        self.center_title()
        self.update_board()

    def center_title(self):
        self.penup()
        self.goto(-10, 270)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", move=False, align=TITLE_ALIGNMENT, font=TITLE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=TITLE_ALIGNMENT, font=TITLE_FONT)