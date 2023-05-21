# This program is a flash-card game that helps to learn 100 most common
# spanish words with english translation. The UI is done with Tkinter.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

from tkinter import *
import csv
import pandas
import random

BACKGROUND_COLOR = "#B1ddC6"
LANGUAGE_FONT = ("Ariel", 30, "italic")
DEFINITION_font = ("Ariel", 40, "bold")
current_card = {}

# --------------------- DATA HANDLER ------------------ #
try:
    data = pandas.read_csv("data/left_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_english_words2.csv")

to_learn = data.to_dict(orient="records")

# --------------------- MANAGER ----------------------- #


def generate_card():
    # card will flip to show the translation after 3 seconds
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_language, text="Spanish")
    canvas.itemconfig(card_defin, text=f'{current_card["rank"]} : {current_card["spanish"]}')
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=turn_card)


def turn_card():
    canvas.itemconfig(card_language, text='English')
    canvas.itemconfig(card_defin, text=current_card["english"])
    canvas.itemconfig(card_bg, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    print(data)
    data.to_csv("data/left_to_learn.csv", index=False)

    generate_card()

# --------------------- UI TKINTER -------------------- #
# 2x2 grid.
window = Tk()
window.title("Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Turn card every 3 seconds
flip_timer = window.after(3000, func=turn_card)

# Card
canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="images/card_back.png")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_language = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)  # position relative to canvas
card_defin = canvas.create_text(400, 263, text="", font=DEFINITION_font)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=generate_card)
wrong_btn.grid(row=1, column=1)

# the first thing pop up is the word
generate_card()
window.mainloop()



