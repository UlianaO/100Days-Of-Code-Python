# This event driven program utilizes the famous Pomodoro technique of time management,
# that helps with information retentions and motivates to get done more.
# 4 sets of 25-minite work with 5-minute break, 30 minutes after 5th set
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """ Resets timer text, checkmarks, title label """
    start_but["state"] = "active"
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_but["state"] = "disabled"  # disable the button so no parallel timer is running
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)  # min * 60 = seconds.
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """ Recursive function takes in the number of seconds"""
    minutes = math.floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    # gets into canvas, timer_text is a part of canvas to be changed
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmarks.config(text="✔" * int(reps / 2))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # x pos, y, pos,
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)


start_but = Button()
start_but.config(text="Start", command=start_timer, highlightthickness=0, bg=GREEN, fg="white", font=(FONT_NAME, 15, "bold"))
start_but.grid(column=0, row=3)

reset_but = Button()
reset_but.config(text="Reset", command=reset_timer, highlightthickness=0, bg=GREEN, fg="white", font=(FONT_NAME, 15, "bold"))
reset_but.grid(column=3, row=3)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=2, row=4)
window.mainloop()