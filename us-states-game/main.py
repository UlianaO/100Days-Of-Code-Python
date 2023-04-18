# A simple game to see if the player knows all 50 states.
# Player puts in the state, and the game shows if it exists and places it onto the right location on the map.

import turtle
import pandas

BACKGROUND = "blank_states_img.gif"

# ************** GETTING COORDINATES OF EACH STATE ********************* #
# # Prints coordinates of states on the background image
# def get_coordinates(x, y):
#     print(x, y)
#
# # Listen to mouse click on the background, prints out the coordinates
# turtle.onscreenclick(get_coordinates)
# turtle.mainloop()

# Base Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)

# Read data
data = pandas.read_csv("50_states.csv")

# Collect all states from csv:
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:

    # Creates a pop-up box
    answer_state = screen.textinput(title=f"{len(guess_states)}/50", prompt="What is your state guess?").title()
    if answer_state == "Exit" or None:
        break
    # Check if in database
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # returns and stores a row of data
        print(state_data)
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))

        t.write(answer_state)


# Once the game is over, show the states that were bot guessed by the player during the game so they can learn.
# Compare guessed states with all_states.
missed_states = []
for state in all_states:
    if state not in guess_states:
        missed_states.append(state)

# Save missed states to CSV
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()



