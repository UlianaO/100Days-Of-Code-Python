
PLACEHOLDER = "[name]"  # string to replace inside of the letter

# Turn names in names.txt to a list of names using readlines()
with open("./Input/names.txt") as nfile:
    names = nfile.readlines()

with open("./Input/letter.txt") as lfile:
    letter = lfile.read()
    # Go through each name, replacing placeholder in the letter with the name from the list.
    # Each name(except for the last one) contains new line at the end - use strip() to get rid of them.
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        # Create a letter for each name in the list.
        with open(f"./ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)




