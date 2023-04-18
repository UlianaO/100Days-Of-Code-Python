from turtle import Turtle

TITLE_ALIGNMENT = "center"
TITLE_FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Screen class
        self.score = 0
        with open("high_score.txt") as data:
            self.highest_score = int(data.read())
        self.hideturtle()
        self.center_title()
        self.update_board()

    def center_title(self):
        self.penup()
        self.goto(-10, 270)

    def update_score(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest: {self.highest_score}", move=False, align=TITLE_ALIGNMENT, font=TITLE_FONT)

    def reset_game(self):
        # Save the current score as the highest if greater.
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        # Reset the score
        self.score = 0
        self.update_board()
