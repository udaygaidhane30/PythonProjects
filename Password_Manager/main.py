from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for word in range(randint(8, 10))]
    password_symbol = [choice(symbols) for symbol in range(randint(2, 4))]
    password_number = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_input = website_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": username_input,
            "password": password_input,
        }
    }
    if len(password_input) == 0 or len(website_input) == 0:
        messagebox.showerror(title="error", message="Fill all details")

    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details you entered:\n"
                                                                    f"Username = {username_input}\n"
                                                                    f"Password = {password_input}\nIs is ok?")
        if is_ok:
            # password_file.write(f"{website_input} : username--> {username_input} | password--> {
            # password_input}\n")
            try:
                with open("password_file.json", mode="r") as password_file:
                    data = json.load(password_file)

            except FileNotFoundError:
                with open("password_file.json", mode="w") as password_file:
                    json.dump(new_data, password_file, indent=4)

            else:
                data.update(new_data)
                with open("password_file.json", mode="w") as password_file:
                    json.dump(data, password_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.insert(0, "day.gaidhane0934@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
