# This is a guess-who-wins game created with the help of Turtle library.

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_choice = screen.textinput(title="Make your bet", prompt="Enter color of the turtle")
colors = ["blue", "red", "orange", "green", "yellow", "black"]
game_on = False
all_turtles = []

#  Create many turtle objects out of the Turtle class
y_position = -70  # starting with y = -100
for index in range(0, 6):
    tommy = Turtle(shape="turtle")
    all_turtles.append(tommy)
    tommy.color(colors[index])  # 6 turtles, 6 colors
    tommy.penup()
    tommy.goto(x=-230, y=y_position)
    y_position = y_position + 30

if user_choice:
    game_on = True

while game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"You`ve won! The {winner} came first.")
            else:
                print("You`ve lost, sorry!")

        distance = random.randint(0, 20)
        turtle.forward(distance)

screen.exitonclick()
