# The game is created to practice basic python syntax.
# The idea is to have a user guess who has higher amount of Instagram Followers.
# The data is stores in data.py file

import random
from data import data  # file data.py, list 'data'
from logo import logo_game_name



# Format data.
def format_data(person):
    """ Formats the person`s data """
    return f'{person["name"]}, a {person["description"]}, from {person["country"]}.'


def compare_followers(a, b):
    """ Returns a person with the higher follower count"""
    if a["follower_count"] > b["follower_count"]:
        return a
    elif a["follower_count"] == b["follower_count"]:
        return
    else:
        return b


# Keep track of the user`s score
current_score = 0
keep_going = True
# Putting it out of the while loop so every time it prints at the top of the terminal.
person_b = random.choice(data)
# Show logo.
print(logo_game_name)

while (keep_going):

    # Generate two random picks for comparison.
    person_a = person_b
    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)

    print(f"Compare A: {format_data(person_a)}.")
    print(f"Against B: {format_data(person_b)}.")

    user_choice = input("Who do you think has more followers? A or B:   \n").title()
    winner = compare_followers(person_a, person_b)  # returns a sublist

    if user_choice == 'A':
        user_choice = person_a
    elif user_choice == 'B':
        user_choice = person_b
    else:
        print("Wrong input")


    if winner == user_choice:
        # User winning count is updated
        current_score += 1
        print(f'\nYou`re right! Current score is: {current_score}\n')
    else:
        print('Sorry, you lost :(')
        keep_going = False

print(f"Your final score is {current_score}")
    # prompt the user to pick.
    # update their score if the pick is right. if wrong - terminate the program
