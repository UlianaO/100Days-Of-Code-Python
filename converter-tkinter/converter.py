from tkinter import *
# check

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # adds space around edges


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label()
miles_label.config(text="Miles", padx=10, pady=10)
miles_label.grid(column=2, row=0)

text_l = Label()
text_l.config(text="is equal to", padx=10, pady=10)
text_l.grid(column=0, row=1)

result_l = Label()
result_l.config(text="", padx=10, pady=10)
result_l.grid(column=1, row=1)

km_l = Label()
km_l.config(text="Km", padx=10, pady=10)
km_l.grid(column=2, row=1)


def calculate_clicked():
    # Converts miles to KM
    miles = miles_input.get()
    km = float(miles)*1.609344
    result_l.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(column=2, row=3)

window.mainloop()
