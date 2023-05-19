from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR -------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [choice(letters) for _ in range(randint(6, 10))]
    pwd_nums = [choice(numbers) for _ in range(randint(2, 4))]
    pwd_syms = [choice(symbols) for _ in range(randint(2, 4))]

    password_generated = pwd_syms + pwd_nums + pwd_letters
    shuffle(password_generated)
    print(password_generated)

    password = "".join(password_generated)

    password_ent.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """ Saves info from entries into passwords.txt and emtpies the entries"""
    website = website_ent.get()
    email = email_ent.get()
    password = password_ent.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="You left some empty field")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"Your details: \n Email: {email} \n "
                                                      f"Password: {password} \n Save?")

        if is_okay:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{website} | {email} |  {password}\n")
                website_ent.delete(0, END)
                password_ent.delete(0, END)

# ---------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

# Entries
website_ent = Entry()
website_ent.grid(column=1, row=1, columnspan=2, sticky="EW")

email_ent = Entry()
email_ent.grid(column=1, row=2, columnspan=2, sticky="EW")
email_ent.insert(0, "ulyana.ozerova@gmail.com")

password_ent = Entry()
password_ent.grid(column=1, row=3, sticky="EW")

# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()