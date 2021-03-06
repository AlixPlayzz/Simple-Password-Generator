import random
import string
import time
from tkinter import *

Root = Tk()
Root.geometry("400x400")
Root.title("Random Password Generator")
Root.config(bg="darkgoldenrod")
Root.resizable(False, False)

option_characters = "none"
option_numbers = "none"
option_length = 4

title_label = Label(Root, text="Password Generator", font=("Minecraft", 20, 'bold'))
title_label.pack(pady=10)
title_label.config(bg="peachpuff")

options_label = Label(Root, text="Options:", font=("Minecraft", 20, 'italic'), bg="peachpuff")
options_label.pack(pady=10)

different_options = Label(Root, text='''Type "N" = Enable Numbers
Type "C" = Enable Characters
Type "L:<Number>" = Number of Characters. (Default=4)''')
different_options.pack(pady=0.1)

options_entry = Entry(width=30)
options_entry.pack(pady=10)

random_characters = "none"
random_numbers = "none"


def generate_pass():
    global random_numbers
    global random_characters
    if option_numbers == "true":
        numbers1 = string.digits
        global option_characters
        if option_characters == "true":
            random_numbers = (''.join(random.choice(numbers1) for i in range(int(option_length / 2))))
        else:
            random_numbers = (''.join(random.choice(numbers1) for i in range(int(option_length))))
    if option_characters == "true":
        letters1 = string.ascii_letters
        if option_numbers == "true":
            random_characters = (''.join(random.choice(letters1) for i in range(int(option_length / 2))))
        else:
            random_characters = (''.join(random.choice(letters1) for i in range(int(option_length))))
    final_password = random_characters + random_numbers
    print("The generated password is: " + final_password)
    final_pass_label = Text(Root)
    final_pass_label.configure(state="normal")
    if option_length > 20:
        final_pass_label.config(height=1, width=40)
    else:
        final_pass_label.config(height=1, width=20)
    final_pass_label.insert(END, final_password)
    final_pass_label.place(relx="0.5", rely="0.53", anchor="center")
    final_pass_label.configure(state="disabled")


generate_button = Button(text="Generate", height=2, width=40, command=generate_pass)
generate_button.pack(pady=80)


def submit_options():
    value_options_entry = options_entry.get()
    if value_options_entry == "C":
        global option_characters
        option_characters = "true"
        print("The users input is 'C'. Characters Enabled.")
    if value_options_entry == "N":
        global option_numbers
        option_numbers = "true"
        print("The users input is 'N'. Numbers Enabled.")
    if "L" in value_options_entry:
        a, b = value_options_entry.split(':')
        global option_length
        option_length = int(b)
        print("The users input is: " + b + ". Length of password set.")


submit_options()

submit_button = Button(text="Submit", command=submit_options)
submit_button.place(relx="0.5", rely="0.6", anchor="center")

mainloop()
